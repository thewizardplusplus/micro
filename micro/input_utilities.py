import fileinput
import sys

import string_utilities

def read_code(filename='-'):
    return ''.join(line for line in fileinput.input(filename))

def read_input(bytes_number):
    return string_utilities.make_list_from_string(
        sys.stdin.read(int(bytes_number) if bytes_number is not None else None),
    )
