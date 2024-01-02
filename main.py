import sys
import ast
import json
from Constructors.Pattern import *
from Constructors.Policy import *
from Constructors.Multilabelling import *
from Constructors.Multilabel import *
from Visitor import *

def analyze_code(tree, vulnerabilities, policy):

    testVisitor = Visitor(tree, vulnerabilities, policy)

    multilabel = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            multilabel = testVisitor.visit_Constant(node)

        elif isinstance(node, ast.Name):
            multilabel = testVisitor.visit_Name(node)

        elif isinstance(node, ast.BinOp):
            multilabel = testVisitor.visit_BinOp(node)

        elif isinstance(node, ast.UnaryOp):
            multilabel = testVisitor.visit_UnaryOp(node)

        elif isinstance(node, ast.BoolOp):
            multilabel = testVisitor.visit_BoolOp(node)

        elif isinstance(node, ast.Compare):
            multilabel = testVisitor.visit_Compare(node)
            
        elif isinstance(node, ast.Call):
            multilabel = testVisitor.visit_Call(node)

        elif isinstance(node, ast.Attribute):
            multilabel = testVisitor.visit_Attribute(node)

        elif isinstance(node, ast.Expr):
            multilabel = testVisitor.visit_Expr(node)

        elif isinstance(node, ast.Assign):
            multilabel = testVisitor.visit_Assign(node)

        elif isinstance(node, ast.If):
            multilabel = testVisitor.visit_If(node)

        elif isinstance(node, ast.While):
            multilabel = testVisitor.visit_While(node)



def main():

    # Receives two arguments
    # - Python file containing the program to be analysed
    # - Name of the JSON file containing the list of vulnerability patterns

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        print("Usage: python3 file vulnerabilities")
        sys.exit(1)

    pythonFile = sys.argv[1]
    vulFile = sys.argv[2]
    outputFile = "./output/" + pythonFile[:-3] + ".output.json"


    # verify the types of the files
    if pythonFile[-3:] != ".py":
        print("First argument should be a python file")
        sys.exit(1)
    if vulFile[-13:] != "patterns.json":
        print("Second argument should be a JSON file")
        sys.exit(1)

    python_content = None
    vul_content = None
    # try to open the files while checking if they exists
    try:
        with open(pythonFile, 'r') as file:
            python_content = file.read()
    except FileNotFoundError:
        print(f"The file '{pythonFile}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        with open(vulFile, 'r') as file:
            vul_content = json.load(file)
    except FileNotFoundError:
        print(f"The file '{vulFile}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    
    ast_tree = ast.parse(python_content)
    ast_json = json.loads(json.dumps(ast_tree, default=lambda x: x.__dict__))

    policy = Policy([])
    vulnerabilities = None
    if (len(vul_content) == 0):
        vulnerabilities = []
    else:
        for i in range(len(vul_content)):
            p=vul_content[i]
            policy.add_pattern(Pattern(p["vulnerability"], p["sources"], p["sanitizers"], p["sinks"]))
    
    #with open("ast.json", "w", encoding="utf-8") as outfile:
    #    json.dump(ast_json, outfile, indent=1)

    #analyze_code(ast_tree, vulnerabilities, policy)

    label1 = Labels().add_source("a")
    label2 = Labels().add_source("b")
    p1 = Pattern("a", "b", "c", "d")

    Multilabel1 = Multilabel([p1])
    Multilabel1.add_source(p1,"a")
    Multilabel2 = Multilabel([p1])
    Multilabel2.add_source(p1,"b")
    Multilabel1 = Multilabel1.combine(Multilabel2, vulnerabilities)
    print(Multilabel1)


    test_Visitor = Visitor(ast_tree, vulnerabilities, policy)
    test_Visitor.visit(ast_tree)

    with open(outputFile, "w", encoding="utf-8") as outfile:
        json.dump(vulnerabilities, outfile, indent=1)

    sys.exit(1)

if __name__ == "__main__":
    main()