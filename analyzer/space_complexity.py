import ast

def estimate_space_complexity(file_path):
    """
    Estimate space complexity based on memory allocations
    - Lists, dicts, sets, tuples, arrays
    Returns a rough estimate: O(1), O(n), or O(n^2)
    """
    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)
    count = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if isinstance(node.value, (ast.List, ast.Dict, ast.Set, ast.Tuple)):
                count += 1
            elif isinstance(node.value, ast.Call) and getattr(node.value.func, 'id', '') in ['list', 'dict', 'set', 'tuple']:
                count += 1

    if count == 0:
        return "O(1)"
    elif count <= 3:
        return "O(n)"
    else:
        return "O(n^2)"
