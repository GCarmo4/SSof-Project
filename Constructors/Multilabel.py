import Label

class MultiLabel(Label):
    def __init__(self, patterns):
        self.pattern_labels = {pattern.pattern_name: Label() for pattern in patterns}

    def add_source(self, pattern_name, source_name):
        if pattern_name in self.pattern_labels and source_name in self.pattern_labels[pattern_name].valid_sources:
            self.pattern_labels[pattern_name].add_source(source_name)

    def add_sanitizer(self, pattern_name, sanitizer_name):
        if pattern_name in self.pattern_labels and sanitizer_name in self.pattern_labels[pattern_name].valid_sanitizers:
            self.pattern_labels[pattern_name].add_sanitizer(sanitizer_name)

    def combine(self, other_multi_label):
        combined_multi_label = MultiLabel([])

        for pattern_name in self.pattern_labels:
            if pattern_name in other_multi_label.pattern_labels:
                combined_label = self.pattern_labels[pattern_name].combine(other_multi_label.pattern_labels[pattern_name])
                combined_multi_label.pattern_labels[pattern_name] = combined_label

        return combined_multi_label

    def __str__(self):
        return "\n".join([f"{pattern_name}:\n{label}" for pattern_name, label in self.pattern_labels.items()])
