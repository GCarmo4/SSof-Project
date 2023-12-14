import ast
import inspect
import sample_code

def traverse_ast(node, depth=0):
    """
    Recursively traverse the AST and print node type and line number.

    Parameters:
    - node (ast.AST): The current AST node.
    - depth (int): The depth of the node in the AST.

    Returns:
    - None
    """
    if isinstance(node, ast.AST):
        # Print node type and line number
        print(f"{'  ' * depth}Type: {type(node).__name__}, Line: {node.lineno if hasattr(node, 'lineno') else 'N/A'}")

        # Recursively traverse child nodes
        for child_node_name, child_node in ast.iter_fields(node):
            if isinstance(child_node, list):
                for idx, child in enumerate(child_node):
                    print(f"{'  ' * (depth + 1)}{child_node_name}[{idx}]:")
                    traverse_ast(child, depth + 2)
            elif isinstance(child_node, ast.AST):
                print(f"{'  ' * (depth + 1)}{child_node_name}:")
                traverse_ast(child_node, depth + 2)

def main():
    # Get the source code of the module
    source_code = inspect.getsource(sample_code)

    # Parse the source code into an AST
    ast_tree = ast.parse(source_code)

    # Traverse and print AST information
    traverse_ast(ast_tree)

if __name__ == "__main__":
    main()
