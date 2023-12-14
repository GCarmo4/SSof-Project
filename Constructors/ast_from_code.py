# pip install astexport

import ast
from astexport import Exporter


def get_ast_from_code(code):
    
    return ast.parse(code)

def convert_ast_to_json(ast_tree):
    exporter = Exporter()
    return exporter.export_dict(ast_tree)

def main():
    # Example Python code
    python_code = """
    def example_function(x):
        if x > 0:
            return x
        else:
            return -x
    """

    # Parse code into AST
    # python_code = código doq estivermos a analisar
    ast_tree = get_ast_from_code(python_code)

    # Convert AST to JSON
    json_representation = convert_ast_to_json(ast_tree)

    # Output JSON
    print(json_representation)

    # este output dá pra ver no site http://jsonviewer.stack.hu/
if __name__ == "__main__":
    main()
