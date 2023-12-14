class Vulnerabilities:
    def __init__(self):
        
        self.vulnerabilities_dict = {}

    def report_vulnerability(self, name, multilabel):
        
        if name not in self.vulnerabilities_dict:
            self.vulnerabilities_dict[name] = []

        # Save the vulnerability information
        self.vulnerabilities_dict[name].append(multilabel)

    def get_vulnerabilities(self):
        
        return self.vulnerabilities_dict


# Example usage:
# Assuming you have a Multilabel object named 'example_multilabel' and a name 'example_name' (ou seja isto é testar já com alguma coisa criada)
vulnerabilities_collector = Vulnerabilities()
vulnerabilities_collector.report_vulnerability("SQL Injection", example_multilabel)
vulnerabilities_collector.report_vulnerability("XSS Attack", another_multilabel)

# Get all detected vulnerabilities
detected_vulnerabilities = vulnerabilities_collector.get_vulnerabilities()
print(detected_vulnerabilities)
