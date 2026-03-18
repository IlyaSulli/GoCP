import ast
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


def goc(clone):
    # Step 1: Parse the function string into an AST
    tree = ast.parse(clone)

    # Step 2: Set a .parent attribute on every node to aid look ups for parent-child relationships
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    # Step 3: Build a directed weighted graph of non-terminal nodes.
    # Each non-terminal node becomes a graph node with a unique integer ID.
    # A directed edge from parent to child is added for every parent-child
    # relationship between two non-terminal nodes. The edge weight counts
    # how many times that dependency appears (increments if seen again).
    graph = nx.DiGraph()
    node_to_id = {}
    next_id = 0

    for node in ast.walk(tree):
        if isinstance(node, NON_TERMINAL_NODES):
            if id(node) not in node_to_id:
                node_to_id[id(node)] = next_id
                graph.add_node(next_id, type=type(node).__name__)
                next_id += 1

    for node in ast.walk(tree):
        if isinstance(node, NON_TERMINAL_NODES):
            parent = getattr(node, "parent", None)
            if parent is not None and isinstance(parent, NON_TERMINAL_NODES):
                parent_id = node_to_id[id(parent)]
                child_id = node_to_id[id(node)]
                if graph.has_edge(parent_id, child_id):
                    graph[parent_id][child_id]["weight"] += 1
                else:
                    graph.add_edge(parent_id, child_id, weight=1)

    return graph
