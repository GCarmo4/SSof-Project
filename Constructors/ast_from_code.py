import ast
import json
import sample_code

def get_ast_from_code(code):
    """
    Parse Python code and return the AST.

    Parameters:
    - code (str): Python code as a string.

    Returns:
    - ast.Module: The root of the AST.
    """
    return ast.parse(code)


def convert_ast_to_json(ast_tree):
    """
    Convert AST to JSON format.

    Parameters:
    - ast_tree (ast.Module): The root of the AST.

    Returns:
    - str: JSON representation of the AST.
    """
    return json.dumps(ast_tree, default=lambda x: x.__dict__)


def main():
    # Example Python code
    python_code = """
def calculate_square(x):
    return x ** 2

number = 5
result = calculate_square(number)
print(f"The square of {number} is {result}")
    """

    # Parse code into AST
    # python_code = cÃ³digo doq estivermos a analisar
    ast_tree = get_ast_from_code(python_code)

    # Convert AST to JSON
    json_representation = convert_ast_to_json(ast_tree)

    # Output JSON
    print(json_representation)


if __name__ == "__main__":
    main() 
