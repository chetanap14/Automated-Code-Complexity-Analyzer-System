import ast

def function_complexity(file_path):
    """
    Analyze each function separately and calculate cyclomatic complexity
    Returns a dictionary: {function_name: complexity_score}
    """
    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)
    results = {}

    class FuncVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            complexity = 1  # start with 1
            for n in ast.walk(node):
                if isinstance(n, (ast.If, ast.For, ast.While, ast.Try)):
                    complexity += 1
                elif isinstance(n, ast.BoolOp):  # and/or
                    complexity += 1
            results[node.name] = complexity
            self.generic_visit(node)

    FuncVisitor().visit(tree)
    return results
           
