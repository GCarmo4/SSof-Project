class Sink:

    def __init__(self, name, line):
        self.name = name
        self.line = line

    def __str__(self):
        return f"{self.name} at line {self.line}"