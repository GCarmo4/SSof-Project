from Constructors.Label import *

class Multilabel():
    def __init__(self, patterns):
        self.pattern_labels = {}
        for pattern in patterns:
            self.pattern_labels[pattern] = Labels()
        self.pattern_sinks = {}

    def add_source(self, pattern, source):
        self.pattern_labels[pattern].add_source(source)

    def get_source(self, pattern):
        if pattern in self.pattern_labels.keys():
            return self.pattern_labels[pattern].get_sources()
        else:
            return []

    def add_sanitizer(self, pattern, sanitizer_name):
        if (pattern in self.pattern_labels.keys()) and (sanitizer_name not in self.pattern_labels[pattern].sanitizers):
            self.pattern_labels[pattern].add_sanitizer(sanitizer_name)

    def add_patterns_sink(self, patterns, sink, vulnerabilities, multilabelling):
        
        for pattern in patterns:
            if pattern not in self.pattern_sinks.keys():
                self.pattern_sinks[pattern] = []
            if sink.name not in self.pattern_labels[pattern].get_source_names():
                self.pattern_sinks[pattern] += [sink]
        if self.has_illegal_flow():
            vulnerabilities.report_vulnerability(self)

    def combine(self, other_multi_label, vulnerabilities, combine_sink = True):
        combined_multi_label = Multilabel([])
        for pattern in self.pattern_labels:
            combined_multi_label.pattern_labels[pattern] = self.pattern_labels[pattern].combine(other_multi_label.pattern_labels[pattern])
        if combine_sink:
            if len(self.pattern_sinks) != 0:
                combined_multi_label.pattern_sinks = self.pattern_sinks
            if len(other_multi_label.pattern_sinks) != 0:
                for p in other_multi_label.pattern_sinks.keys():
                    if p in combined_multi_label.pattern_sinks.keys():
                        
                        combined_multi_label.pattern_sinks[p] += other_multi_label.pattern_sinks[p]
                        combined_multi_label.pattern_sinks[p] = list(set(combined_multi_label.pattern_sinks[p]))
                    else:
                        
                        combined_multi_label.pattern_sinks[p] = other_multi_label.pattern_sinks[p]
        if combined_multi_label.has_illegal_flow():
            vulnerabilities.report_vulnerability(combined_multi_label)
            combined_multi_label.pattern_sinks = {}
        return combined_multi_label
    
    def has_illegal_flow(self):
        temp = self.pattern_sinks.copy()
        for pattern in self.pattern_sinks:
            temp_list = temp[pattern].copy()
            if self.pattern_labels[pattern].is_empty():
                temp.pop(pattern)
        return len(temp) != 0
    
    def get_pattern_names(self):
        patterns = self.pattern_labels.keys()
        names = []
        for pattern in patterns:
            names.append(self.pattern_labels[pattern])
        return names
    
    def is_sink(self, sink_name):
        for pattern in self.pattern_labels:
            if pattern.is_sink(sink_name):
                return True
        return False

    def is_source(self, source_name):
        for pattern in self.pattern_labels:
            if pattern.is_source(source_name):
                return True
        return False
    
    def is_source_in_labels(self, source_name):
        for pattern in self.pattern_labels:
            if source_name in self.pattern_labels[pattern].get_source_names():
                return True
        return False

    def __str__(self):
        return "\n".join([f"{pattern_name}:\n{label}" for pattern_name, label in self.pattern_labels.items()])
