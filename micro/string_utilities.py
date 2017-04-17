import re
import type_utilities
import list_utilities

STRING_CHARACTER_PATTERN = r'\\["\\tn]|(?!\\)[^"]'

_ESCAPING_MAP = {'"': r'\"', '\\': r'\\', '\t': r'\t', '\n': r'\n'}
_UNESCAPING_MAP = {value: key for key, value in _ESCAPING_MAP.items()}
_STRING_CHARACTER_COMPILED_PATTERN = re.compile(STRING_CHARACTER_PATTERN)

def quote(string):
    return '"' + ''.join([_ESCAPING_MAP.get(character, character) for character in string]) + '"'

def unquote(string):
    return _STRING_CHARACTER_COMPILED_PATTERN.sub(lambda matches: _UNESCAPING_MAP.get(matches.group(), matches.group()), string[1:-1])

def get_representation(value):
    representation = ''
    if value is None:
        representation = 'nil'
    elif isinstance(value, float):
        representation = _get_number_representation(value)
    elif type_utilities.is_list(value):
        representation = _get_list_representation(value, get_representation)
    elif type_utilities.is_pack(value):
        representation = _get_pack_representation(value)
    elif type_utilities.is_closure(value):
        representation = _get_closure_representation(value)
    else:
        raise Exception('the unknown type ' + value.__class__.__name__)

    return representation

def get_string_list_representation(string_list):
    return _get_list_representation(string_list, lambda item: quote(make_string_from_list(item)))

def make_list_from_string(string):
    return list_utilities.reduce_list(string, lambda symbol: float(ord(symbol)))

def make_string_from_list(pair):
    items = list_utilities.map_list(pair, lambda symbol: chr(int(symbol)))
    return ''.join(items)

def _get_list_representation(pair, handler):
    items = list_utilities.map_list(pair, handler)
    return '[' + ', '.join(items) + ']'

def _get_number_representation(number):
    # must not combine a stripping
    return str(number).rstrip('0').rstrip('.')

def _get_pack_representation(pack):
    return '(' + get_representation(pack[0]) + ')'

def _get_closure_representation(function):
    return '<closure {:#x}>'.format(id(function))
