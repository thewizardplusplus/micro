import re
import type_utilities
import functools

STRING_CHARACTER_PATTERN = r'\\["\\tn]|(?!\\)[^"]'

_ESCAPING_MAP = {'"': r'\"', '\\': r'\\', '\t': r'\t', '\n': r'\n'}
_UNESCAPING_MAP = {value: key for key, value in _ESCAPING_MAP.items()}
_STRING_CHARACTER_COMPILED_PATTERN = re.compile(STRING_CHARACTER_PATTERN)

def quote(string):
    return '"' + ''.join([_ESCAPING_MAP.get(character, character) for character in string]) + '"'

def unquote(string):
    return _STRING_CHARACTER_COMPILED_PATTERN.sub(lambda matches: _UNESCAPING_MAP.get(matches.group(), matches.group()), string[1:-1])

def get_representation(value):
    return str(value) if not type_utilities.is_list(value) else _get_list_representation(value)

def make_list_from_string(string):
    return functools.reduce(lambda pair, character: (character, pair), map(ord, reversed(string)), ())

def make_string_from_list(pair):
    items = _map_list(pair, chr)
    return ''.join(items)

def _get_list_representation(pair):
    items = _map_list(pair, get_representation)
    return '[' + ', '.join(items) + ']'

def _map_list(pair, handler):
    items = []
    while len(pair) > 0:
        item = handler(pair[0])
        items.append(item)

        pair = pair[1]

    return items
