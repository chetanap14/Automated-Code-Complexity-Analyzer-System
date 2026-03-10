import ast

def count_loops(file_path):

    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)

    count = 0

    for node in ast.walk(tree):
        if isinstance(node, (ast.For, ast.While)):
            count += 1

    return count
