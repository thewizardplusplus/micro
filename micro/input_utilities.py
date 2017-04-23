import fileinput
import sys

import string_utilities

def read_code(filename='-'):
    return ''.join(line for line in fileinput.input(filename))

def read_input(symbols_number):
    return _read_symbols(sys.stdin.read, symbols_number)

def read_input_line(symbols_number):
    return _read_symbols(sys.stdin.readline, symbols_number)

def _read_symbols(reader, number):
    return string_utilities.make_list_from_string(
        reader(int(number) if number is not None and number >= 0 else -1),
    )
