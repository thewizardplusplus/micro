import sys

import type_utilities
import string_utilities

class Error:
    def __init__(self, description, offset):
        self._description = description
        self._offset = offset

    def __str__(self):
        try:
            return 'error({}; {}): {}'.format(
                self._line,
                self._column,
                self._description,
            )
        except AttributeError:
            return 'error({}): {}'.format(self._offset, self._description)

    def detect_position(self, code):
        right_code = code[0:self._offset]
        self._line = right_code.count('\n') + 1
        self._column = self._offset - right_code.rfind('\n')

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

def process_errors(errors, code):
    for some_error in errors:
        some_error.detect_position(code)
        sys.stderr.write(str(some_error) + '\n')

    if len(errors) != 0:
        sys.exit(1)
