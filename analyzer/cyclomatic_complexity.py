import ast

def calculate_cyclomatic_complexity(file_path):

    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)

    complexity = 1

    for node in ast.walk(tree):

        if isinstance(node, (ast.If, ast.For, ast.While, ast.And, ast.Or)):
            complexity += 1

    return complexity









"""
import ast

def calculate_cyclomatic_complexity(file_path):

    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)

    complexity = 1

    class ComplexityVisitor(ast.NodeVisitor):

        def visit_If(self, node):
            nonlocal complexity
            complexity += 1
            self.generic_visit(node)

        def visit_For(self, node):
            nonlocal complexity
            complexity += 1
            self.generic_visit(node)

        def visit_While(self, node):
            nonlocal complexity
            complexity += 1
            self.generic_visit(node)

        def visit_BoolOp(self, node):
            nonlocal complexity
            complexity += 1
            self.generic_visit(node)

        def visit_Try(self, node):
            nonlocal complexity
            complexity += 1
            self.generic_visit(node)

    visitor = ComplexityVisitor()
    visitor.visit(tree)

    return complexity
"""
