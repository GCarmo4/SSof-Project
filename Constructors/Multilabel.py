import Label

class MultiLabel(Label):
    def __init__(self, patterns):
        """
        Constructor for the MultiLabel class.

        Parameters:
        - patterns (list of Pattern): List of patterns corresponding to the multi-label.
        """
        self.pattern_labels = {pattern.pattern_name: Label() for pattern in patterns}

    def add_source(self, pattern_name, source_name):
        """
        Add a source to the label corresponding to the specified pattern.

        Parameters:
        - pattern_name (str): Name of the pattern.
        - source_name (str): Name of the information source.
        """
        if pattern_name in self.pattern_labels and source_name in self.pattern_labels[pattern_name].valid_sources:
            self.pattern_labels[pattern_name].add_source(source_name)

    def add_sanitizer(self, pattern_name, sanitizer_name):
        """
        Add a sanitizer to the label corresponding to the specified pattern.

        Parameters:
        - pattern_name (str): Name of the pattern.
        - sanitizer_name (str): Name of the sanitizer.
        """
        if pattern_name in self.pattern_labels and sanitizer_name in self.pattern_labels[pattern_name].valid_sanitizers:
            self.pattern_labels[pattern_name].add_sanitizer(sanitizer_name)

    def combine(self, other_multi_label):
        """
        Combine two multi-labels and return a new multi-label representing the combined information integrity.

        Parameters:
        - other_multi_label (MultiLabel): Another multi-label to combine with.

        Returns:
        - MultiLabel: New multi-label representing the combined information integrity.
        """
        combined_multi_label = MultiLabel([])

        for pattern_name in self.pattern_labels:
            if pattern_name in other_multi_label.pattern_labels:
                combined_label = self.pattern_labels[pattern_name].combine(other_multi_label.pattern_labels[pattern_name])
                combined_multi_label.pattern_labels[pattern_name] = combined_label

        return combined_multi_label

    def __str__(self):
        """
        String representation of the MultiLabel object.

        Returns:
        - str: String representation of the MultiLabel.
        """
        return "\n".join([f"{pattern_name}:\n{label}" for pattern_name, label in self.pattern_labels.items()])
