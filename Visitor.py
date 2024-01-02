import ast
from BaseVisitor import *
from Constructors.Multilabel import *
from Constructors.Multilabelling import *
from Constructors.Source import *
from Constructors.Sink import *

class Visitor (BaseVisitor):

    def __init__(self, root, vulnerabilities, policy):
        super().__init__(root, vulnerabilities, policy)
        self.multilabelling = Multilabelling()
        self.policy = policy
    
    def visit(self, expr):
        return self.multilabelling.get_multilabel_for_name(expr)

    def check_iflow(self, name, lineno, multilabel, implicit: bool = False):
        iflow = self.policy.get_illegal_flows(name,multilabel, implicit)
        
        if len(iflow.pattern_labels) != 0:
            self.vulnerabilities.add_vulnerability_by_multilabel(iflow, Sink(name,lineno))

    def visit_Constant(self, node):
        multilabel = Multilabel([])
        return multilabel

    def visit_Name(self, node):
        if node.id in self.policy.get_all_sources():
            patterns = self.policy.get_patterns_for_source(node.id)
            multilabel = Multilabel(patterns)
            for pattern in patterns:
                multilabel.add_source(pattern, Source(node.id, node.lineno))
        patterns_for_sink = []
        patterns_for_sink = self.policy.get_pattern_sink(node.id)
        if len(patterns_for_sink) != 0:
            multilabel = Multilabel([])
            multilabel.add_patterns_sink(patterns_for_sink, Sink(node.id, node.lineno))


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
        multilabel = self.visit(node.func)
        if multilabel is None:
            multilabel = Multilabel([])

        for arg in node.args:
            arg_multilabel = self.visit(arg)
            if arg_multilabel is None:
                arg_multilabel = Multilabel([])
            multilabel = multilabel.combine(arg_multilabel)
        
        return multilabel

    def visit_Attribute(self, node):
        value_multilabel = self.visit(node.value)
        if value_multilabel is None:
            value_multilabel = Multilabel([])

        return value_multilabel


    def visit_Expr(self, node):
        multilabel = self.visit(node.value)
        if multilabel is None:
            multilabel = Multilabel([])
        return multilabel

    def visit_Assign(self, node):
        multilabel = self.visit(node.value)
        if multilabel is None:
            multilabel = Multilabel([])
        
        for target in node.targets:
            self.multilabelling.update_multilabel_for_name(target, multilabel)

        return multilabel
    
    def visit_If(self, node):
        multilabel = self.visit(node.test)
        if multilabel is None:
            multilabel = Multilabel([])

        return multilabel

    def visit_While(self, node):
        temp = self.multilabelling

        multilabel = self.visit(node.test)
        if multilabel is None:
            multilabel = Multilabel([])
        

        return multilabel