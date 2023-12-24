import ast

def traverse_ast_with_traces(node, traces=[], current_trace=[]):
    """
    Recursively traverse the AST and print sets of complete traces.

    Parameters:
    - node (ast.AST): The current AST node.
    - traces (list): List to store sets of complete traces.
    - current_trace (list): The current trace being built.

    Returns:
    - None
    """
    if isinstance(node, ast.AST):
        # Append current node to the current trace
        current_trace.append(type(node).__name__)

        # Case analysis on node type
        if isinstance(node, ast.While):
            # Handle while loop (considering a constant maximum number of repetitions)
            max_repetitions = 3
            for i in range(min(max_repetitions, 2)):
                traverse_ast_with_traces(node.body, traces, current_trace.copy())
        else:
            # Recursively traverse child nodes
            for child_node_name, child_node in ast.iter_fields(node):
                if isinstance(child_node, list):
                    for child in child_node:
                        traverse_ast_with_traces(child, traces, current_trace.copy())
                elif isinstance(child_node, ast.AST):
                    traverse_ast_with_traces(child_node, traces, current_trace.copy())

def main():
    # Example Python code
    python_code = """
    x = 5
    while x > 0:
        print(x)
        x -= 1
    print("Done")
    """

    # Parse code into AST
    ast_tree = ast.parse(python_code)
    # denovo, python_code é o codigo que for pra dar traverse
    
    # Traverse and print sets of complete traces
    traces = []
    traverse_ast_with_traces(ast_tree, traces)

    # Print the sets of complete traces
    for i, trace in enumerate(traces, 1):
        print(f"Trace {i}: {trace}")

if __name__ == "__main__":
    main()
