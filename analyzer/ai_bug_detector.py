import ast

def detect_ai_bugs(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    tree = ast.parse(code)

    bugs = []

    for node in ast.walk(tree):

        # empty loop
        if isinstance(node, (ast.For, ast.While)):
            if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                bugs.append("Empty loop detected")

        # infinite loop
        if isinstance(node, ast.While):
            if isinstance(node.test, ast.Constant) and node.test.value == True:
                bugs.append("Possible infinite loop")

        # empty exception
        if isinstance(node, ast.ExceptHandler):
            if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                bugs.append("Exception ignored (pass in except)")

        # unused variable detection
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if target.id == "_":
                        bugs.append("Unused variable detected")

    return bugs
