from Constructors.Label import *

class Multilabel():
    def __init__(self, patterns):
        print("patterns:", patterns)
        self.pattern_labels = {pattern: Labels() for pattern in patterns}
        self.pattern_sinks = {}

    def add_source(self, pattern, source):
        if (pattern in self.pattern_labels.keys()) and (source not in self.pattern_labels[pattern].sources):
            self.pattern_labels[pattern].add_source(source)

    def get_source(self, pattern):
        if pattern in self.pattern_labels.keys():
            return self.pattern_labels[pattern].get_sources()
        else:
            return []

    def add_sanitizer(self, pattern, sanitizer_name):
        if (pattern in self.pattern_labels.keys()) and (sanitizer_name not in self.pattern_labels[pattern].sanitizers):
            self.pattern_labels[pattern].add_sanitizer(sanitizer_name)

    def add_patterns_sink(self, patterns, sink, vulnerabilities):
        for pattern in patterns:
            self.pattern_sinks[pattern] = sink
        if self.has_illegal_flow():
            vulnerabilities.report_vulnerability(self)

    def combine(self, other_multi_label, vulnerabilities):
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
        if len(self.pattern_sinks) != 0:
            combined_multi_label.pattern_sinks = self.pattern_sinks
        if len(other_multi_label.pattern_sinks) != 0:
            combined_multi_label.pattern_sinks = other_multi_label.pattern_sinks
        if combined_multi_label.has_illegal_flow():
            vulnerabilities.report_vulnerability(combined_multi_label)
        return combined_multi_label
    
    def has_illegal_flow(self):
        for pattern in self.pattern_sinks:
            if pattern not in self.pattern_labels:
                self.pattern_sinks.pop(pattern)
        return len(self.pattern_sinks) != 0
    
    def get_pattern_names(self):
        patterns = self.pattern_labels.keys()
        names = []
        for pattern in patterns:
            names.append(self.pattern_labels[pattern])
        return names

    def __str__(self):
        return "\n".join([f"{pattern_name}:\n{label}" for pattern_name, label in self.pattern_labels.items()])
