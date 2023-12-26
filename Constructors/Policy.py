import MultiLabel

class Policy:
    def __init__(self, patterns):
        self.patterns = patterns

    def get_all_vulnerabilities(self):
        return [pattern.vulnerability_name for pattern in self.patterns]

    def get_sources_for_vulnerability(self, vulnerability_name):
        sources = [pattern.source_names for pattern in self.patterns if pattern.vulnerability_name == vulnerability_name]
        return sources[0] if sources else []

    def get_sanitizers_for_vulnerability(self, vulnerability_name):
        sanitizers = [pattern.sanitizer_names for pattern in self.patterns if pattern.vulnerability_name == vulnerability_name]
        return sanitizers[0] if sanitizers else []

    def get_sinks_for_vulnerability(self, vulnerability_name):
        sinks = [pattern.sink_names for pattern in self.patterns if pattern.vulnerability_name == vulnerability_name]
        return sinks[0] if sinks else []

    def illegal_flows(self, name, multilabel):
        illegal_multilabel = MultiLabel([])

        for pattern in self.patterns:
            if name in pattern.sink_names and name in multilabel.get_sources():
                illegal_multilabel.pattern_labels[pattern.vulnerability_name] = multilabel.pattern_labels[pattern.vulnerability_name]

    def illegal_flows_for_program_counter(self, name, multilabel):
        illegal_multilabel = MultiLabel([])

        for pattern in self.patterns:
            if name in pattern.sink_names and multilabel.has_source(pattern.source_names):
                illegal_multilabel.pattern_labels[pattern.vulnerability_name] = multilabel.pattern_labels[pattern.vulnerability_name]

        return illegal_multilabel
