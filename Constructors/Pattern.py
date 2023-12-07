import Label
class Pattern:
    def __init__(self, vulnerability_name, source_names, sanitizer_names, sink_names):
        """
        Constructor for the Pattern class.

        Parameters:
        - vulnerability_name (str): Name of the vulnerability pattern.
        - source_names (list of str): List of possible source names.
        - sanitizer_names (list of str): List of possible sanitizer names.
        - sink_names (list of str): List of possible sink names.
        """
        self.vulnerability_name = vulnerability_name
        self.source_names = source_names
        self.sanitizer_names = sanitizer_names
        self.sink_names = sink_names

    def get_vulnerability_name(self):
        """
        Get the vulnerability name.

        Returns:
        - str: Vulnerability name.
        """
        return self.vulnerability_name

    def set_vulnerability_name(self, new_name):
        """
        Set the vulnerability name.

        Parameters:
        - new_name (str): New vulnerability name.
        """
        self.vulnerability_name = new_name

    def get_source_names(self):
        """
        Get the list of possible source names.

        Returns:
        - list of str: List of possible source names.
        """
        return self.source_names

    def set_source_names(self, new_sources):
        """
        Set the list of possible source names.

        Parameters:
        - new_sources (list of str): New list of possible source names.
        """
        self.source_names = new_sources

    def get_sanitizer_names(self):
        """
        Get the list of possible sanitizer names.

        Returns:
        - list of str: List of possible sanitizer names.
        """
        return self.sanitizer_names

    def set_sanitizer_names(self, new_sanitizers):
        """
        Set the list of possible sanitizer names.

        Parameters:
        - new_sanitizers (list of str): New list of possible sanitizer names.
        """
        self.sanitizer_names = new_sanitizers

    def get_sink_names(self):
        """
        Get the list of possible sink names.

        Returns:
        - list of str: List of possible sink names.
        """
        return self.sink_names

    def set_sink_names(self, new_sinks):
        """
        Set the list of possible sink names.

        Parameters:
        - new_sinks (list of str): New list of possible sink names.
        """
        self.sink_names = new_sinks

    def is_source(self, name):
        """
        Check if the given name is a source for the pattern.

        Parameters:
        - name (str): Name to be checked.

        Returns:
        - bool: True if the name is a source, False otherwise.
        """
        return name in self.source_names

    def is_sanitizer(self, name):
        """
        Check if the given name is a sanitizer for the pattern.

        Parameters:
        - name (str): Name to be checked.

        Returns:
        - bool: True if the name is a sanitizer, False otherwise.
        """
        return name in self.sanitizer_names

    def is_sink(self, name):
        """
        Check if the given name is a sink for the pattern.

        Parameters:
        - name (str): Name to be checked.

        Returns:
        - bool: True if the name is a sink, False otherwise.
        """
        return name in self.sink_names


    def __str__(self):
        """
        String representation of the Pattern object.

        Returns:
        - str: String representation of the Pattern.
        """
        return f"Vulnerability: {self.vulnerability_name}\nSources: {self.source_names}\nSanitizers: {self.sanitizer_names}\nSinks: {self.sink_names}"