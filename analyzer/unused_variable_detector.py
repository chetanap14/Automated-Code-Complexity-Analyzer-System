import ast

def detect_unused_variables(file_path):
    
    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)

    assigned = set()
    used = set()

    class VariableVisitor(ast.NodeVisitor):

        def visit_Assign(self, node):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assigned.add(target.id)
            self.generic_visit(node)

        def visit_Name(self, node):
            used.add(node.id)
            self.generic_visit(node)

    visitor = VariableVisitor()
    visitor.visit(tree)

    unused = assigned - used
    return list(unused)
