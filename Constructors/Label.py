class Labels (object):

    def __init__(self):
        self.sources = []
        self.sanitizers = {}

    def add_source(self, source_name):
        sources = []
        for source in self.sources:
            sources += [source.name]
        if source_name.name in sources:
            i = self.get_source_index_by_name(source_name.name)
            self.sources[i].line = source_name.line
        else:
            self.sources.append(source_name)

    def is_empty(self):
        return len(self.sources) == 0

    def add_sanitizer(self, sanitizer_name):
        self.sanitizers[sanitizer_name] = self.sources.copy()

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
        
    def get_source_index_by_name(self, source_name):
        count = 0
        for s in self.sources:
            if s.name == source_name:
                return count
            count += 1

    def combine(self, other_label):
        temp_other = other_label.sanitizers.copy()
        combined_label = Labels()
        combined_label.sources = self.sources.copy() + other_label.get_sources().copy()
        combined_label.sanitizers = self.sanitizers.copy()
        for key, value in temp_other.items():
            if key in combined_label.sanitizers:
                combined_label.sanitizers[key] += value
            else:
                combined_label.sanitizers[key] = value
        return combined_label
    
    def get_sanitizers_for_source(self, source):
        sanitizers = []
        for sanitizer in self.sanitizers:
            if source in self.sanitizers[sanitizer]:
                sanitizers += [sanitizer]
        return sanitizers
    
    def __str__(self):
        return f"Sources: {self.sources}\nSanitizers: {self.sanitizers}"