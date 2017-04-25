import sys
import os.path
import copy

from . import type_utilities
from . import string_utilities
from . import options

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
        self._filename = os.path.relpath(filename)

    def detect_position(self, code):
        right_code = code[0:self._offset]
        self._line = right_code.count('\n') + 1
        self._column = self._offset - right_code.rfind('\n')

    def _has_attributes(self, attributes):
        return all(hasattr(self, attribute) for attribute in attributes)

def update_errors(errors, code, filename=None):
    return (_update_error(error, code, filename) for error in errors)

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

def _update_error(error, code, filename=None):
    updated_error = copy.copy(error)
    updated_error.detect_position(code)
    if filename is not None:
        updated_error.set_filename(options.get_script_name(filename))

    return updated_error
