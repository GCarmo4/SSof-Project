from Constructors.Multilabel import *
from Constructors.Label import *
from Constructors.Sanitizer import *
from Constructors.Sink import *

class Vulnerabilities:
    def __init__(self):
        
        self.vulnerabilities = []

    def report_vulnerability(self, multilabel):
        # Save the vulnerability information
        patterns = list(multilabel.pattern_sinks.keys())
        for pattern in patterns:
            for source in multilabel.pattern_labels[pattern].sources:
                print(multilabel.pattern_sinks[pattern])
                if not multilabel.pattern_labels[pattern].is_empty():
                    vulnerability = {}
                    vulnerability["vulnerability"] = pattern.vulnerability_name
                    vulnerability["source"] = (source.name, source.line)
                    sink = multilabel.pattern_sinks[pattern]
                    vulnerability["sink"] = (sink.name, sink.line)
                    if len(multilabel.pattern_labels[pattern].sources) == len(multilabel.pattern_labels[pattern].sanitizers):
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