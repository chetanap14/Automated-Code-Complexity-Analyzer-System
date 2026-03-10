import ast


def detect_loop_depth(code):

    # If code is list of lines convert to string
    if isinstance(code, list):
        code = "\n".join(code)

    tree = ast.parse(code)

    max_depth = 0

    def visit(node, depth):

        nonlocal max_depth

        if isinstance(node, (ast.For, ast.While)):
            depth += 1
            max_depth = max(max_depth, depth)

        for child in ast.iter_child_nodes(node):
            visit(child, depth)

    visit(tree, 0)

    return max_depth
            

