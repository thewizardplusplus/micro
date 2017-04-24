import sys

import type_utilities
import string_utilities

class Error:
    def __init__(self, description, offset):
        self._description = description
        self._offset = offset

    def __str__(self):
        error_mark = ''
        if self._has_attributes(['_filename', '_line', '_column']):
            error_mark = '{}; {}; {}'.format(
                self._filename,
                self._line,
                self._column,
            )
        elif self._has_attributes(['_line', '_column']):
            error_mark = '{}; {}'.format(self._line, self._column)
        else:
            error_mark = str(self._offset)

        return 'error({}): {}'.format(error_mark, self._description)

    def set_filename(self, filename):
        self._filename = filename

    def detect_position(self, code):
        right_code = code[0:self._offset]
        self._line = right_code.count('\n') + 1
        self._column = self._offset - right_code.rfind('\n')

    def _has_attributes(self, attributes):
        return all(hasattr(self, attribute) for attribute in attributes)

def exit(status):
    if status is None:
        # zero equivalent
        pass
    elif isinstance(status, float) and 0 <= status <= 127:
        status = int(status)
    elif type_utilities.is_list(status):
        status = string_utilities.make_string_from_list(status)
    else:
        raise Exception(
            'the incorrect exit status {}'.format(status.__class__.__name__),
        )

    sys.exit(status)

def process_errors(errors, code, filename):
    for some_error in errors:
        some_error.detect_position(code)
        some_error.set_filename(filename)

        sys.stderr.write(str(some_error) + '\n')

    if len(errors) != 0:
        sys.exit(1)
