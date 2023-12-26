import ast
import json
from your_module_containing_classes import MultiLabel, Policy, Vulnerabilities

def process_expression(node, policy, multilabel, vulnerabilities, program_counter_multilabel):
    if isinstance(node, ast.BinOp):
        left_multilabel = process_expression(node.left, policy, multilabel, vulnerabilities, program_counter_multilabel)
        right_multilabel = process_expression(node.right, policy, multilabel, vulnerabilities, program_counter_multilabel)
        result_multilabel = left_multilabel.combine(right_multilabel)
        return result_multilabel

    elif isinstance(node, ast.Call):
        function_name = node.func.id if isinstance(node.func, ast.Name) else None
        if function_name:
            relevant_patterns = policy.get_sink_patterns_for_function(function_name)
            if relevant_patterns:
                for arg in node.args:
                    arg_multilabel = process_expression(arg, policy, multilabel, vulnerabilities, program_counter_multilabel)
                    for pattern in relevant_patterns:
                        illegal_flow = policy.illegal_flows(function_name, arg_multilabel, program_counter_multilabel)
                        if illegal_flow:
                            vulnerabilities.report_vulnerability(pattern.vulnerability_name, illegal_flow)
        return multilabel.get_multilabel_for_name(function_name)

    elif isinstance(node, ast.Assign):
        target_name = node.targets[0].id if isinstance(node.targets[0], ast.Name) else None
        value_multilabel = process_expression(node.value, policy, multilabel, vulnerabilities, program_counter_multilabel)
        multilabel.update_multilabel_for_name(target_name, value_multilabel)
        return value_multilabel

# Example usage in your main function
def main():
    # Assuming you have a list of patterns
    patterns = [...]  # Replace [...] with your actual patterns

    # Initialize Policy, MultiLabelling, and Vulnerabilities objects
    policy = Policy(patterns)
    multilabel = MultiLabel(patterns)
    vulnerabilities = Vulnerabilities()

    # Mock program counter multilabel (modify based on your actual implementation)
    program_counter_multilabel = MultiLabel(patterns)

    # Read and import AST (assuming you have a function to do this)
    ast_tree = sample_code.get_ast_from_code("your_python_program.py")

    # Traverse AST and process expressions
    for node in ast.walk(ast_tree):
        if isinstance(node, ast.Expr):
            process_expression(node, policy, multilabel, vulnerabilities, program_counter_multilabel)

    # Display results
    print("Multilabel after processing expressions:")
    print(multilabel)

    print("Detected vulnerabilities:")
    print(vulnerabilities.get_vulnerabilities())

if __name__ == "__main__":
    main()
