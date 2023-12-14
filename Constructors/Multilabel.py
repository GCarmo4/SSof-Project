import Label

class MultiLabel():
    def __init__(self, patterns):
        self.pattern_labels = {pattern: Label() for pattern in patterns}

    def add_source(self, pattern, source_name):
        if pattern in self.pattern_labels and source_name in self.pattern_labels[pattern].valid_sources:
            self.pattern_labels[pattern].add_source(source_name)

    def add_sanitizer(self, pattern, sanitizer_name):
        if pattern in self.pattern_labels and sanitizer_name in self.pattern_labels[pattern].valid_sanitizers:
            self.pattern_labels[pattern].add_sanitizer(sanitizer_name)

    def combine(self, other_multi_label):
        combined_multi_label = MultiLabel([])

        for pattern in self.pattern_labels:
            if pattern in other_multi_label.pattern_labels:
                combined_label = self.pattern_labels[pattern].combine(other_multi_label.pattern_labels[pattern])
                combined_multi_label.pattern_labels[pattern] = combined_label

        return combined_multi_label
    
    def get_pattern_names(self):
        patterns = self.pattern_labels.keys()
        names = []
        for pattern in patterns:
            names += [pattern.pattern_name]
        return names

    def __str__(self):
        return "\n".join([f"{pattern_name}:\n{label}" for pattern_name, label in self.pattern_labels.items()])
