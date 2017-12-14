import re
import fileinput
import sys

from . import string_utilities

_SHEBANG_PATTERN = re.compile(r'^#!.*?(?:\r\n|\n\r|\n|\r)')

def read_code(filename='-'):
    return ''.join(line for line in fileinput.input(filename))

def read_input(symbols_number):
    return _read_symbols(sys.stdin.read, symbols_number)

def read_input_line(symbols_number):
    return _read_symbols(sys.stdin.readline, symbols_number)

def remove_shebang(code):
    return _SHEBANG_PATTERN.sub('', code)

def _read_symbols(reader, number):
    return string_utilities.make_list_from_string(
        reader(int(number) if number is not None and number >= 0 else -1),
    )
