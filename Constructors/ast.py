import ast
import json
from MultiLabel import MultiLabel
from Policy import Policy
from Vulnerabilities import Vulnerabilities

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

def process_statement(node, policy, multilabel, vulnerabilities, program_counter_multilabel):
    if isinstance(node, ast.Assign):
        target_name = node.targets[0].id if isinstance(node.targets[0], ast.Name) else None
        value_multilabel = process_expression(node.value, policy, multilabel, vulnerabilities, program_counter_multilabel)
        multilabel.update_multilabel_for_name(target_name, value_multilabel)

    elif isinstance(node, ast.If):
        test_multilabel = process_expression(node.test, policy, multilabel, vulnerabilities, program_counter_multilabel)

        true_branch_multilabel = multilabel.copy()
        false_branch_multilabel = multilabel.copy()

        true_branch_multilabel = process_statements(node.body, policy, true_branch_multilabel, vulnerabilities, program_counter_multilabel)

        if node.orelse:
            false_branch_multilabel = process_statements(node.orelse, policy, false_branch_multilabel, vulnerabilities, program_counter_multilabel)

        merged_multilabel = true_branch_multilabel.combine(test_multilabel, false_branch_multilabel)

        return merged_multilabel

    elif isinstance(node, ast.While):
        test_multilabel = process_expression(node.test, policy, multilabel, vulnerabilities, program_counter_multilabel)
        body_multilabel = multilabel.copy()

        for _ in range(10):  # ajustar numero depois
            body_multilabel = process_statements(node.body, policy, body_multilabel, vulnerabilities, program_counter_multilabel)

        multilabel = multilabel.combine(test_multilabel, body_multilabel)

    return multilabel

def process_statements(statements, policy, multilabel, vulnerabilities, program_counter_multilabel):
    for statement in statements:
        multilabel = process_statement(statement, policy, multilabel, vulnerabilities, program_counter_multilabel)

    return multilabel

def main():
    # meter a lista de patterns
    patterns = [...] 

    # inicializar
    policy = Policy(patterns)
    multilabel = MultiLabel(patterns)
    vulnerabilities = Vulnerabilities()

    program_counter_multilabel = MultiLabel(patterns)

    # ler e importar o codigo e usar a otura function pra ir buscar
    ast_tree = sample_code.get_ast_from_code("your_python_program.py")

    # fazer o traverse
    for node in ast.walk(ast_tree):
        if isinstance(node, ast.Expr):
            process_expression(node, policy, multilabel, vulnerabilities, program_counter_multilabel)

    process_statements(ast_tree.body, policy, multilabel, vulnerabilities, program_counter_multilabel

    # mostrar nha resultado
    print("Multilabel after processing expressions:")
    print(multilabel)

    print("Detected vulnerabilities:")
    print(vulnerabilities.get_vulnerabilities())

if __name__ == "__main__":
    main()
