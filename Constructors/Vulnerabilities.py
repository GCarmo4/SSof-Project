from Constructors.Multilabel import *
from Constructors.Label import *
from Constructors.Sanitizer import *
from Constructors.Sink import *

class Vulnerabilities:
    def __init__(self):
        
        self.vulnerabilities = []
        self.vulnerabilities_multilabel = []

    def report_vulnerability(self, multilabel):
        self.vulnerabilities_multilabel += [multilabel]
        # Save the vulnerability information
        patterns = list(multilabel.pattern_sinks.keys())
        for pattern in patterns:
            for source in multilabel.pattern_labels[pattern].sources:
                for sink in multilabel.pattern_sinks[pattern]:
                    if not multilabel.pattern_labels[pattern].source_in_sanitizer(source):
                        multilabel.pattern_labels[pattern].unsanitized_illegal_flows += 1
                    if not multilabel.pattern_labels[pattern].is_empty():
                        vulnerability = {}
                        vulnerability["vulnerability"] = pattern.vulnerability_name
                        vulnerability["source"] = [source.name, source.line]
                        vulnerability["sink"] = [sink.name, sink.line]
                        if multilabel.pattern_labels[pattern].unsanitized_illegal_flows == 0:
                            vulnerability["unsanitized_flows"] = "no"
                        else:
                            vulnerability["unsanitized_flows"] = "yes"
                        sanitizers = multilabel.pattern_labels[pattern].get_sanitizers_for_source(source)
                        vul_sanitizer = []
                        for sanitizer in sanitizers:
                            vul_sanitizer += [[sanitizer.name, sanitizer.line]]
                        vulnerability["sanitized_flows"] = vul_sanitizer
                        #sanitized
                        self.vulnerabilities += [vulnerability]

    def get_vulnerabilities(self):
        
        return self.vulnerabilities_dict
    
    def get_all_sinks(self):
        sinks = []
        for v in self.vulnerabilities:
            sinks += v["sink"][0]
        return sinks
    
    def get_source_sink(self):
        pairs = []
        for v in self.vulnerabilities:
            pairs += [[v["sink"][0], v["source"][0]]]
        return pairs