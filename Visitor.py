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
    
    #def visit(self, expr):
    #    return self.multilabelling.get_multilabel_for_name(expr)

    def check_iflow(self, name, lineno, multilabel, implicit: bool = False):
        iflow = self.policy.get_illegal_flows(name,multilabel, implicit)
        
        if len(iflow.pattern_labels) != 0:
            self.vulnerabilities.add_vulnerability_by_multilabel(iflow, Sink(name,lineno))

    def visit_Constant(self, node):
        multilabel = Multilabel(self.policy.patterns)
        return multilabel

    def visit_Name(self, node):
        multilabel = Multilabel(self.policy.patterns)
        print(node.id)
        if node.id in self.policy.get_all_sources():
            print("here")
            patterns = self.policy.get_patterns_for_source(node.id)
            for pattern in patterns:
                multilabel.add_source(pattern, Source(node.id, node.lineno))
                print("source", multilabel.pattern_labels[pattern])
        patterns_for_sink = []
        patterns_for_sink = self.policy.get_pattern_sink(node.id)
        if len(patterns_for_sink) != 0:
            print("AHAHAHAH")
            multilabel.add_patterns_sink(patterns_for_sink, Sink(node.id, node.lineno), self.vulnerabilities)
            print("sssss", multilabel.pattern_sinks)

        return multilabel
        #if node.id in self.policy.get_all_sinks():
        # ainda n descobri o q fzr / como, c os sinks


    def visit_BinOp(self, node):
        multilabel = self.visit(node.left)
        if multilabel is None:
            multilabel = Multilabel(self.policy.patterns)
        right_multilabel = self.visit(node.right)
        if right_multilabel is None:
            right_multilabel = Multilabel(self.policy.patterns)
        multilabel = multilabel.combine(right_multilabel, self.vulnerabilities)
        return multilabel

    def visit_UnaryOp(self, node):
        multilabel = self.visit(node.operand)
        if multilabel is None:
            multilabel = Multilabel(self.policy.patterns)
        return multilabel

    def visit_BoolOp(self, node):
        multilabel = self.visit(node.values[0])
        if multilabel is None:
            multilabel = Multilabel(self.policy.patterns)
        for i in range(1, len(node.values)):
            val_multilabel = self.visit(node.values[i])
            if val_multilabel is None:
                val_multilabel = Multilabel(self.policy.patterns)
            multilabel = multilabel.combine(val_multilabel, self.vulnerabilities)
        return multilabel

    def visit_Compare(self, node):
        multilabel = self.visit(node.left)
        for comp in node.comparators:
            comp_multilabel = self.visit(comp)
            if comp_multilabel is None:
                comp_multilabel = Multilabel(self.policy.patterns)
            multilabel = multilabel.combine(comp_multilabel, self.vulnerabilities)
        return multilabel

    def visit_Call(self, node):
        print("call")
        multilabel = self.visit(node.func)
        print("call1", multilabel)
        if multilabel is None:
            multilabel = Multilabel(self.policy.patterns)

        for arg in node.args:
            arg_multilabel = self.visit(arg)
            if arg_multilabel is None:
                arg_multilabel = Multilabel(self.policy.patterns)
            multilabel = multilabel.combine(arg_multilabel, self.vulnerabilities)
        print("call2", multilabel)
        return multilabel

    def visit_Attribute(self, node):
        value_multilabel = self.visit(node.value)
        if value_multilabel is None:
            value_multilabel = Multilabel(self.policy.patterns)

        return value_multilabel


    def visit_Expr(self, node):
        multilabel = self.visit(node.value)
        if multilabel is None:
            multilabel = Multilabel(self.policy.patterns)
        return multilabel

    def visit_Assign(self, node):
        print("assign")
        multilabel = self.visit(node.value)
        print("assign1", multilabel)
        if multilabel is None:
            multilabel = Multilabel(self.policy.patterns)
        
        for target in node.targets:
            self.multilabelling.update_multilabel_for_name(target, multilabel)

        print("assign2", multilabel.pattern_sinks)
        return multilabel
    
    def visit_If(self, node):
        multilabel = self.visit(node.test)
        if multilabel is None:
            multilabel = Multilabel(self.policy.patterns)

        return multilabel

    def visit_While(self, node):
        temp = self.multilabelling

        multilabel = self.visit(node.test)
        if multilabel is None:
            multilabel = Multilabel(self.policy.patterns)
        

        return multilabel