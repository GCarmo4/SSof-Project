import MultiLabel

class Policy:
    def __init__(self, patterns):
        """
        Constructor for the Policy class.

        Parameters:
        - patterns (list of Pattern): List of vulnerability patterns to be considered.
        """
        self.patterns = patterns

    def get_all_vulnerabilities(self):
        """
        Get all the vulnerability names considered by the policy.

        Returns:
        - list of str: List of vulnerability names.
        """
        return [pattern.vulnerability_name for pattern in self.patterns]

    def get_sources_for_vulnerability(self, vulnerability_name):
        """
        Get source names for a specific vulnerability.

        Parameters:
        - vulnerability_name (str): Name of the vulnerability.

        Returns:
        - list of str: List of source names for the specified vulnerability.
        """
        sources = [pattern.source_names for pattern in self.patterns if pattern.vulnerability_name == vulnerability_name]
        return sources[0] if sources else []

    def get_sanitizers_for_vulnerability(self, vulnerability_name):
        """
        Get sanitizer names for a specific vulnerability.

        Parameters:
        - vulnerability_name (str): Name of the vulnerability.

        Returns:
        - list of str: List of sanitizer names for the specified vulnerability.
        """
        sanitizers = [pattern.sanitizer_names for pattern in self.patterns if pattern.vulnerability_name == vulnerability_name]
        return sanitizers[0] if sanitizers else []

    def get_sinks_for_vulnerability(self, vulnerability_name):
        """
        Get sink names for a specific vulnerability.

        Parameters:
        - vulnerability_name (str): Name of the vulnerability.

        Returns:
        - list of str: List of sink names for the specified vulnerability.
        """
        sinks = [pattern.sink_names for pattern in self.patterns if pattern.vulnerability_name == vulnerability_name]
        return sinks[0] if sinks else []

    def illegal_flows(self, name, multilabel):
        """
        Determine illegal flows for a given name and multilabel.

        Parameters:
        - name (str): Name for which illegal flows are determined.
        - multilabel (MultiLabel): Multilabel describing information flow.

        Returns:
        - MultiLabel: New multilabel with labels only for patterns with illegal flows.
        """
        illegal_multilabel = MultiLabel([])

        for pattern in self.patterns:
            if name in pattern.sink_names and name in multilabel.get_sources():
                illegal_multilabel.pattern_labels[pattern.vulnerability_name] = multilabel.pattern_labels[pattern.vulnerability_name]

        return illegal_multilabel
