import MultiLabel

class MultiLabelling:
    def __init__(self, initial_mapping=None):
        self.labelling_map = initial_mapping if initial_mapping else {}

    def get_multilabel_for_name(self, variable_name):
        return self.labelling_map.get(variable_name, MultiLabel([]))

    def update_multilabel_for_name(self, variable_name, new_multilabel):
        self.labelling_map[variable_name] = new_multilabel

    def __str__(self):
        return "\n".join([f"{variable_name}: {multilabel}" for variable_name, multilabel in self.labelling_map.items()])

# Example usage:
pattern1 = Pattern("Pattern1", ["user_input", "http_request"], ["sanitize_sql", "escape_string"])
pattern2 = Pattern("Pattern2", ["input_data", "file_upload"], ["validate_input", "check_file_type"])

# Create MultiLabelling with initial mapping
initial_mapping = {
    "variable1": MultiLabel([pattern1]),
    "variable2": MultiLabel([pattern2]),
}

multilabelling = MultiLabelling(initial_mapping)

# Get and update multilabel for a variable
current_multilabel = multilabelling.get_multilabel_for_name("variable1")
print(f"Current multilabel for variable1: {current_multilabel}")

new_multilabel = MultiLabel([pattern2])
multilabelling.update_multilabel_for_name("variable1", new_multilabel)

# Display the multilabelling
print("\nCurrent Multilabelling:")
print(multilabelling)
