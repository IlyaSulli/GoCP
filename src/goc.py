import ast

VARIABLE_NODES = (ast.Name, ast.arg, ast.Constant)
OPERATION_NODES = (ast.Assign, ast.AugAssign, ast.Compare, ast.BinOp,
                   ast.UnaryOp, ast.BoolOp, ast.Call, ast.Return,
                   ast.If, ast.For, ast.While)


def goc(clone):
    # Parse the function into an AST
    tree = ast.parse(clone)

    # Extract the nodes (e.g. variables and operations)
    variables = []
    operations = []

    # Look for anything that acts on values or acts as a value and sort them into an array
    for node in ast.walk(tree):
        if isinstance(node, VARIABLE_NODES):
            variables.append(node)
        elif isinstance(node, OPERATION_NODES):
            operations.append(node)
    return
