class Label(object):
    def __init__(self):
        """
        Constructor for the Label class.
        Initializes an empty list of sources and sanitizers.
        """
        self.sources = []
        self.sanitizers = []

    def add_source(self, source_name):
        """
        Add a source to the label.

        Parameters:
        - source_name (str): Name of the information source.
        """
        self.sources.append(source_name)

    def add_sanitizer(self, sanitizer_name):
        """
        Add a sanitizer to the label.

        Parameters:
        - sanitizer_name (str): Name of the sanitizer intercepting the flow.
        """
        self.sanitizers.append(sanitizer_name)

    def get_sources(self):
        """
        Get the list of information sources in the label.

        Returns:
        - list of str: List of information sources.
        """
        return self.sources

    def get_sanitizers(self):
        """
        Get the list of sanitizers intercepting the flows in the label.

        Returns:
        - list of str: List of sanitizers.
        """
        return self.sanitizers

    def get_source_at_index(self, index):
        """
        Get the information source at a specific index.

        Parameters:
        - index (int): Index of the source.

        Returns:
        - str: Information source at the specified index.
        """
        if 0 <= index < len(self.sources):
            return self.sources[index]
        else:
            return None

    def get_sanitizer_at_index(self, index):
        """
        Get the sanitizer at a specific index.

        Parameters:
        - index (int): Index of the sanitizer.

        Returns:
        - str: Sanitizer at the specified index.
        """
        if 0 <= index < len(self.sanitizers):
            return self.sanitizers[index]
        else:
            return None

    def combine(self, other_label):
        """
        Combine two labels and return a new label representing the integrity of information resulting
        from their combination.

        Parameters:
        - other_label (Label): Another label to combine with.

        Returns:
        - Label: New label representing the combined information integrity.
        """
        combined_label = Label()
        combined_label.sources = self.sources.copy() + other_label.get_sources().copy()
        combined_label.sanitizers = self.sanitizers.copy() + other_label.get_sanitizers().copy()
        return combined_label
    
    def __str__(self):
        """
        String representation of the Label object.

        Returns:
        - str: String representation of the Label.
        """
        return f"Sources: {self.sources}\nSanitizers: {self.sanitizers}"

