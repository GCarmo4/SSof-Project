from Constructors.Label import *

class Multilabel():
    def __init__(self, patterns):
        self.pattern_labels = {pattern: Labels() for pattern in patterns}

    def add_source(self, pattern, source_name):
        if (pattern in self.pattern_labels.keys()) and (source_name not in self.pattern_labels[pattern].sources):
            self.pattern_labels[pattern].add_source(source_name)

    def add_sanitizer(self, pattern, sanitizer_name):
        if (pattern in self.pattern_labels.keys()) and (sanitizer_name not in self.pattern_labels[pattern].sanitizers):
            self.pattern_labels[pattern].add_sanitizer(sanitizer_name)

    def combine(self, other_multi_label):
        combined_multi_label = Multilabel([])

        for pattern in self.pattern_labels:
            if pattern in other_multi_label.pattern_labels:
                combined_label = self.pattern_labels[pattern].combine(other_multi_label.pattern_labels[pattern])
                combined_multi_label.pattern_labels[pattern] = combined_label
            else:
                combined_multi_label.pattern_labels[pattern] = self.pattern_labels[pattern]
        for pattern in other_multi_label.pattern_labels:
            if pattern not in combined_multi_label.pattern_labels:
                combined_multi_label.pattern_labels[pattern] = other_multi_label.pattern_labels[pattern]
        return combined_multi_label
    
    def get_pattern_names(self):
        patterns = self.pattern_labels.keys()
        names = []
        for pattern in patterns:
            names.append(self.pattern_labels[pattern])
        return names

    def __str__(self):
        return "\n".join([f"{pattern_name}:\n{label}" for pattern_name, label in self.pattern_labels.items()])
