import ast
class BaseVisitor (ast.NodeVisitor):

    def __init__(self, root: ast.Module):
        self.root = root
        super().__init__()


    def visit_tree(self):
        print("#==================================================#")
        print(f"Visiting tree with: {type(self).__name__}")
        print("---------------------------------------------------")

        super().visit(self.root)

        print("#==================================================#\n")