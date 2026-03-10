import ast

def detect_code_smells(file_path):
    """
    Detect common code smells:
    - Long functions (>50 lines)
    - Too many nested loops (>2)
    - Too many variables in a function (>10)
    Returns a list of warnings
    """
    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)
    smells = []

    class SmellVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            # Long function
            if node.end_lineno - node.lineno > 50:
                smells.append(f"Function '{node.name}' is too long ({node.end_lineno - node.lineno} lines)")

            # Count variables
            vars_in_func = set()
            for n in ast.walk(node):
                if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
                    vars_in_func.add(n.id)
            if len(vars_in_func) > 10:
                smells.append(f"Function '{node.name}' has too many variables ({len(vars_in_func)})")

            # Check nested loops
            max_depth = 0
            def loop_depth(n, current=0):
                nonlocal max_depth
                if isinstance(n, (ast.For, ast.While)):
                    current += 1
                    max_depth = max(max_depth, current)
                for c in ast.iter_child_nodes(n):
                    loop_depth(c, current)
            loop_depth(node)
            if max_depth > 2:
                smells.append(f"Function '{node.name}' has nested loops deeper than 2")

            self.generic_visit(node)

    # Python 3.8+ supports end_lineno
    SmellVisitor().visit(tree)
    return smells
