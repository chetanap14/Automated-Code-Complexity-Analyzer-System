import ast

def detect_recursion(file_path):

    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)

    functions = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions[node.name] = node

    for func_name, func_node in functions.items():
        for node in ast.walk(func_node):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == func_name:
                    return True

    return False
