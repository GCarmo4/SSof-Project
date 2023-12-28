import Constructors.Label as Label
class Pattern:
    def __init__(self, vulnerability_name, source_names, sanitizer_names, sink_names):
        self.vulnerability_name = vulnerability_name
        self.source_names = source_names
        self.sanitizer_names = sanitizer_names
        self.sink_names = sink_names

    def get_vulnerability_name(self):
        return self.vulnerability_name

    def set_vulnerability_name(self, new_name):
        self.vulnerability_name = new_name

    def get_source_names(self):
        return self.source_names

    def set_source_names(self, new_sources):
        self.source_names = new_sources

    def get_sanitizer_names(self):
        return self.sanitizer_names

    def set_sanitizer_names(self, new_sanitizers):
        self.sanitizer_names = new_sanitizers

    def get_sink_names(self):
        return self.sink_names

    def set_sink_names(self, new_sinks):
        self.sink_names = new_sinks

    def is_source(self, name):
        return name in self.source_names

    def is_sanitizer(self, name):
        return name in self.sanitizer_names

    def is_sink(self, name):
        return name in self.sink_names

    def __str__(self):
        return f"Vulnerability: {self.vulnerability_name}\nSources: {self.source_names}\nSanitizers: {self.sanitizer_names}\nSinks: {self.sink_names}"