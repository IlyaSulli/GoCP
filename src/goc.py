import ast
import os
import warnings

import networkx as nx


# Non-terminal AST nodes (structural/statement constructs).
# Leaf nodes (Name, Constant, arg, etc.) are excluded per the GoC paper.
NON_TERMINAL_NODES = (
    ast.FunctionDef,
    ast.AsyncFunctionDef,
    ast.ClassDef,
    ast.Return,
    ast.Assign,
    ast.AugAssign,
    ast.AnnAssign,
    ast.If,
    ast.For,
    ast.AsyncFor,
    ast.While,
    ast.With,
    ast.AsyncWith,
    ast.Try,
    ast.ExceptHandler,
    ast.Import,
    ast.ImportFrom,
    ast.Expr,
    ast.Call,
    ast.BinOp,
    ast.UnaryOp,
    ast.BoolOp,
    ast.Compare,
    ast.IfExp,
    ast.ListComp,
    ast.SetComp,
    ast.DictComp,
    ast.GeneratorExp,
    ast.Yield,
    ast.YieldFrom,
    ast.Raise,
    ast.Assert,
    ast.Delete,
    ast.Global,
    ast.Nonlocal,
)

# Control flow nodes whose bodies create control dependencies
CONTROL_NODES = (
    ast.If,
    ast.For,
    ast.AsyncFor,
    ast.While,
    ast.Try,
    ast.With,
    ast.AsyncWith,
    ast.ExceptHandler,
)


def _def_names(node):
    """Return the set of variable names defined by a non-terminal node."""
    names = set()
    if isinstance(node, ast.Assign):
        for t in node.targets:
            for n in ast.walk(t):
                if isinstance(n, ast.Name):
                    names.add(n.id)
    elif isinstance(node, (ast.AugAssign, ast.AnnAssign)):
        for n in ast.walk(node.target):
            if isinstance(n, ast.Name):
                names.add(n.id)
    elif isinstance(node, (ast.For, ast.AsyncFor)):
        for n in ast.walk(node.target):
            if isinstance(n, ast.Name):
                names.add(n.id)
    elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args = node.args
        for arg in args.args + args.posonlyargs + args.kwonlyargs:
            names.add(arg.arg)
        if args.vararg:
            names.add(args.vararg.arg)
        if args.kwarg:
            names.add(args.kwarg.arg)
    elif isinstance(node, ast.ExceptHandler):
        if node.name:
            names.add(node.name)
    elif isinstance(node, (ast.With, ast.AsyncWith)):
        for item in node.items:
            if item.optional_vars:
                for n in ast.walk(item.optional_vars):
                    if isinstance(n, ast.Name):
                        names.add(n.id)
    elif isinstance(node, ast.NamedExpr):
        names.add(node.target.id)
    return names


def goc(clone, progress=None, filepath=None):
    label = os.path.basename(filepath) if filepath else "unknown"

    # Step 1: Parse the function string into an AST
    if progress:
        progress.status(f"GoC [{label}]: Parsing AST")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SyntaxWarning)
        tree = ast.parse(clone)

    # Step 2: Set parent references on every node
    if progress:
        progress.status(f"GoC [{label}]: Setting parent references")
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    # Step 3: Build graph nodes from non-terminal nodes
    if progress:
        progress.status(f"GoC [{label}]: Building graph nodes")
    graph = nx.DiGraph()
    node_to_id = {}
    next_id = 0

    for node in ast.walk(tree):
        if isinstance(node, NON_TERMINAL_NODES):
            if id(node) not in node_to_id:
                node_to_id[id(node)] = next_id
                graph.add_node(next_id, type=type(node).__name__)
                next_id += 1

    def add_edge(src_id, dst_id):
        if src_id == dst_id:
            return
        if graph.has_edge(src_id, dst_id):
            graph[src_id][dst_id]["weight"] += 1
        else:
            graph.add_edge(src_id, dst_id, weight=1)

    # Step 4: Structural edges — AST parent → child between non-terminal nodes
    if progress:
        progress.status(f"GoC [{label}]: Adding structural edges")
    for node in ast.walk(tree):
        if isinstance(node, NON_TERMINAL_NODES):
            parent = getattr(node, "parent", None)
            if parent is not None and isinstance(parent, NON_TERMINAL_NODES):
                add_edge(node_to_id[id(parent)], node_to_id[id(node)])

    # Step 5: Control dependency edges
    # Each control flow node gets an edge to EVERY non-terminal descendant
    # in its body, not just direct children. This creates the cross-edges
    # that produce triangles (e.g. For → If → Assign but also For → Assign).
    if progress:
        progress.status(f"GoC [{label}]: Adding control dependency edges")
    for node in ast.walk(tree):
        if isinstance(node, CONTROL_NODES) and id(node) in node_to_id:
            ctrl_id = node_to_id[id(node)]
            for desc in ast.walk(node):
                if desc is node:
                    continue
                if isinstance(desc, NON_TERMINAL_NODES) and id(desc) in node_to_id:
                    add_edge(ctrl_id, node_to_id[id(desc)])

    # Step 6: Data dependency edges — def → use for each variable
    # For each Name(Load), find its nearest non-terminal ancestor.
    # For each defining node, add an edge to every use node of that variable.
    if progress:
        progress.status(f"GoC [{label}]: Adding data dependency edges")

    def nearest_nonterminal(n):
        while n is not None:
            if isinstance(n, NON_TERMINAL_NODES) and id(n) in node_to_id:
                return node_to_id[id(n)]
            n = getattr(n, "parent", None)
        return None

    # definitions: var_name -> [node_id, ...]
    definitions = {}
    for node in ast.walk(tree):
        if isinstance(node, NON_TERMINAL_NODES) and id(node) in node_to_id:
            for name in _def_names(node):
                definitions.setdefault(name, []).append(node_to_id[id(node)])

    # uses: var_name -> [node_id, ...]
    uses = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            nt_id = nearest_nonterminal(node)
            if nt_id is not None:
                uses.setdefault(node.id, []).append(nt_id)

    for name, def_ids in definitions.items():
        for use_id in uses.get(name, []):
            for def_id in def_ids:
                add_edge(def_id, use_id)

    return graph
