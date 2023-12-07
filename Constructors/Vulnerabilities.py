class Vulnerabilities:
    def __init__(self):
        """
        Constructor for the Vulnerabilities class.

        Initializes an empty dictionary to store vulnerabilities.
        """
        self.vulnerabilities_dict = {}

    def report_vulnerability(self, name, multilabel):
        """
        Report a detected vulnerability.

        Parameters:
        - name (str): Name representing the detected illegal flows.
        - multilabel (MultiLabel): Multilabel containing sources and sanitizers for the patterns.

        Saves the detected vulnerability in the vulnerabilities dictionary.
        """
        if name not in self.vulnerabilities_dict:
            self.vulnerabilities_dict[name] = []

        # Save the vulnerability information
        self.vulnerabilities_dict[name].append(multilabel)

    def get_vulnerabilities(self):
        """
        Get all detected vulnerabilities.

        Returns:
        - dict: Dictionary containing vulnerabilities organized by vulnerability names.
        """
        return self.vulnerabilities_dict


# Example usage:
# Assuming you have a Multilabel object named 'example_multilabel' and a name 'example_name' (ou seja isto é testar já com alguma coisa criada)
vulnerabilities_collector = Vulnerabilities()
vulnerabilities_collector.report_vulnerability("SQL Injection", example_multilabel)
vulnerabilities_collector.report_vulnerability("XSS Attack", another_multilabel)

# Get all detected vulnerabilities
detected_vulnerabilities = vulnerabilities_collector.get_vulnerabilities()
print(detected_vulnerabilities)
