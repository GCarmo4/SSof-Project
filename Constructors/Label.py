class Labels (object):

    def __init__(self):
        self.sources = []
        self.sanitizers = []

    def add_source(self, source_name):
        self.sources.append(source_name)

    def add_sanitizer(self, sanitizer_name):
        self.sanitizers.append(sanitizer_name)

    def get_sources(self):
        return self.sources

    def get_sanitizers(self):
        return self.sanitizers

    def get_source_at_index(self, index):
        if 0 <= index < len(self.sources):
            return self.sources[index]
        else:
            return None

    def get_sanitizer_at_index(self, index):
        if 0 <= index < len(self.sanitizers):
            return self.sanitizers[index]
        else:
            return None

    def combine(self, other_label):
        combined_label = Labels()
        combined_label.sources = self.sources.copy() + other_label.get_sources().copy()
        combined_label.sanitizers = self.sanitizers.copy() + other_label.get_sanitizers().copy()
        return combined_label
    
    def __str__(self):
        return f"Sources: {self.sources}\nSanitizers: {self.sanitizers}"