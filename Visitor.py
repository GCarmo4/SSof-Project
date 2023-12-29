import ast
import BaseVisitor
import Multilabel
class TestVisitor (BaseVisitor):
    """
    Test visitor class that prints the name of every node it visits.
    """

    def visit_Constant(self, node: ast.Constant) -> None:
        multilabel = Multilabel([])
        return multilabel

    def visit_Name(self, node):
        if node.id in self.policy.get_all_sources():
            patterns = self.policy.get_patterns_for_source(node.id)
            multilabel = Multilabel(patterns)
            for pattern in patterns:
                multilabel.add_source(pattern, node.id)
        #if node.id in self.policy.get_all_sinks():
        # ainda n descobri o q fzr / como, c os sinks


    def visit_BinOp(self, node):
        multilabel = self.visit(node.left)
        if multilabel is None:
            multilabel = Multilabel([])
        right_multilabel = self.visit(node.right)
        if right_multilabel is None:
            right_multilabel = Multilabel([])
        multilabel = multilabel.combine(right_multilabel)
        return multilabel

    def visit_UnaryOp(self, node):
        multilabel = self.visit(node.operand)
        if multilabel is None:
            multilabel = Multilabel([])
        return multilabel

    def visit_BoolOp(self, node):
        multilabel = self.visit(node.values[0])
        if multilabel is None:
            multilabel = Multilabel([])
        for i in range(1, len(node.values)):
            val_multilabel = self.visit(node.values[i])
            if val_multilabel is None:
                val_multilabel = Multilabel([])
            multilabel = multilabel.combine(val_multilabel)
        return multilabel

    def visit_Compare(self, node):
        multilabel = self.visit(node.left)
        for comp in node.comparators:
            comp_multilabel = self.visit(comp)
            if comp_multilabel is None:
                comp_multilabel = Multilabel([])
            multilabel = multilabel.combine(comp_multilabel)
        return multilabel

    def visit_Call(self, node):
        print(f"Visiting Call")
        self.generic_visit(node)

    def visit_Attribute(self, node):
        print(f"Visiting Attribute: {node.attr}")
        self.generic_visit(node)

    def visit_Expr(self, node):
        multilabel = self.visit(node.value)
        if multilabel is None:
            multilabel = Multilabel([])
        return multilabel

    def visit_Assign(self, node):
        print(f"Visiting Assign")
        self.generic_visit(node)

    def visit_If(self, node):
        print(f"Visiting If")
        self.generic_visit(node)

    def visit_While(self, node):
        print(f"Visiting While")
        self.generic_visit(node)