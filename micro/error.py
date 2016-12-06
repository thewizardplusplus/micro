class Error:
    def __init__(self, description, offset):
        self._description = description
        self._offset = offset

    def __str__(self):
        try:
            return 'error({}; {}): {}'.format(self._line, self._column, self._description)
        except AttributeError:
            return 'error({}): {}'.format(self._offset, self._description)

    def detect_position(self, code):
        right_code = code[0:self._offset]
        self._line = right_code.count('\n') + 1
        self._column = self._offset - right_code.rfind('\n')
