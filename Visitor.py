import ast
import BaseVisitor
class TestVisitor (BaseVisitor):
    """
    Test visitor class that prints the name of every node it visits.
    """

    def visit_Constant(self, node: ast.Constant) -> None:
        print(f"Visiting Constant: {node.value}")
        self.generic_visit(node)

    def visit_Name(self, node: ast.Name) -> None:
        print(f"Visiting Name: {node.id}")
        self.generic_visit(node)

    def visit_BinOp(self, node: ast.BinOp) -> None:
        print(f"Visiting BinOp")
        self.generic_visit(node)

    def visit_UnaryOp(self, node: ast.UnaryOp) -> None:
        print(f"Visiting UnaryOp")
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        print(f"Visiting BoolOp")
        self.generic_visit(node)

    def visit_Compare(self, node):
        print(f"Visiting Compare")
        self.generic_visit(node)

    def visit_Call(self, node):
        print(f"Visiting Call")
        self.generic_visit(node)

    def visit_Attribute(self, node):
        print(f"Visiting Attribute: {node.attr}")
        self.generic_visit(node)

    def visit_Expr(self, node):
        print(f"Visiting Expr")
        self.generic_visit(node)

    def visit_Assign(self, node):
        print(f"Visiting Assign")
        self.generic_visit(node)

    def visit_If(self, node):
        print(f"Visiting If")
        self.generic_visit(node)

    def visit_While(self, node):
        print(f"Visiting While")
        self.generic_visit(node)