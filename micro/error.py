class Error:
    def __init__(self, description, line, column):
        self.description = description
        self.line = line
        self.column = column

    def __str__(self):
        return 'error({}; {}): {}'.format(self.line, self.column, self.description)
