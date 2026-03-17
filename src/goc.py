import ast

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
    # Parse the function string into an AST
    tree = ast.parse(clone)

    # Walk the AST in post-order, collecting only non-terminal nodes
    non_terminal_nodes = []
    for node in ast.walk(tree):
        if isinstance(node, NON_TERMINAL_NODES):
            non_terminal_nodes.append(node)

    return non_terminal_nodes
