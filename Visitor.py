import ast
from BaseVisitor import *
from Constructors.Multilabel import *
from Constructors.Multilabelling import *
from Constructors.Source import *
from Constructors.Sink import *
from Constructors.Sanitizer import *

class Visitor (BaseVisitor):

    def __init__(self, root, vulnerabilities, policy):
        super().__init__(root, vulnerabilities, policy)
        self.multilabelling = Multilabelling()
        self.policy = policy
        self.from_call = False
    
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
        in_multilabelling = False
        multilabel = Multilabel(self.policy.patterns)
        if node.id in self.multilabelling.labelling_map:
            in_multilabelling = True
            multilabel = self.multilabelling.get_multilabel_for_name(node.id)
    
        if node.id in self.policy.get_all_sources():
            patterns = self.policy.get_patterns_for_source(node.id)
            for pattern in patterns:
                multilabel.add_source(pattern, Source(node.id, node.lineno))
                print("source", node.id)
        if (node.id not in self.policy.get_all_sources()) and (node.id not in self.multilabelling.labelling_map) and not self.from_call:
            for pattern in multilabel.pattern_labels:
                multilabel.add_source(pattern, Source(node.id, node.lineno))

        patterns_for_sink = []
        patterns_for_sink = self.policy.get_pattern_sink(node.id)
        if (len(patterns_for_sink) != 0) and (node.id not in self.vulnerabilities.get_all_sinks()):
            multilabel.add_patterns_sink(patterns_for_sink, Sink(node.id, node.lineno), self.vulnerabilities, self.multilabelling)


        return multilabel


    def visit_BinOp(self, node):
        multilabel = self.visit(node.left)
        if multilabel is None:
            multilabel = Multilabel(self.policy.patterns)
        right_multilabel = self.visit(node.right)
        if right_multilabel is None:
            right_multilabel = Multilabel(self.policy.patterns)
        multilabel = multilabel.combine(right_multilabel, self.vulnerabilities, False)
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
        self.from_call = True
        multilabel = self.visit(node.func)
        self.from_call = False
        if multilabel is None:
            multilabel = Multilabel(self.policy.patterns)
        for arg in node.args:
            arg_multilabel = self.visit(arg)
            if arg_multilabel is None:
                arg_multilabel = Multilabel(self.policy.patterns)

            multilabel = multilabel.combine(arg_multilabel, self.vulnerabilities)

        for pattern in self.policy.get_patterns_for_sanitizer(node.func.id):
            if not multilabel.pattern_labels[pattern].is_empty():
                multilabel.pattern_labels[pattern].add_sanitizer(Sanitizer(node.func.id, node.lineno))
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
        multilabel = self.visit(node.value)
        if multilabel is None:
            multilabel = Multilabel(self.policy.patterns)
        for tar in node.targets:
            tar_multilabel = self.visit(tar)
            if tar_multilabel is None:
                tar_multilabel = Multilabel(self.policy.patterns)
            multilabel = multilabel.combine(tar_multilabel, self.vulnerabilities)
        
        for target in node.targets:
            if not multilabel.is_source(target.id):
                for pattern in multilabel.pattern_labels:
                    if target.id in multilabel.pattern_labels[pattern].get_source_names():
                        multilabel.pattern_labels[pattern].remove_source(target.id)
            #print("..", multilabel.pattern_labels)
            self.multilabelling.update_multilabel_for_name(target.id, multilabel)
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