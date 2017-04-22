import json
import re

import type_utilities
import list_utilities
import utilities

HEXADECIMAL_ESCAPE_SEQUENCE = r'\\x({}{{2}})'.format(
    utilities.HEXADECIMAL_NUMBER,
)
_HEXADECIMAL_ESCAPE_SEQUENCE = re.compile(HEXADECIMAL_ESCAPE_SEQUENCE)

def quote(string):
    return json.dumps(string)

def unquote(string):
    # force a wrapping of a string to double quotes
    string = '"{}"'.format(string[1:-1])
    # replace ASCII hexadecimal escape sequences to Unicode hexadecimal escape
    # sequences (for a JSON decoding)
    string = _HEXADECIMAL_ESCAPE_SEQUENCE.sub(
        lambda matches: r'\u00{}'.format(matches.group(1)),
        string,
    )
    return json.loads(string)

def get_representation(value):
    representation = ''
    if value is None:
        representation = 'nil'
    elif isinstance(value, float):
        representation = _get_number_representation(value)
    elif type_utilities.is_list(value):
        representation = _get_list_representation(value, get_representation)
    elif isinstance(value, dict):
        representation = get_hash_representation(value)
    elif type_utilities.is_pack(value):
        representation = _get_pack_representation(value)
    elif type_utilities.is_closure(value):
        representation = _get_closure_representation(value)
    else:
        raise Exception('the unknown type {}'.format(value.__class__.__name__))

    return representation

def get_string_representation(pair):
    return quote(make_string_from_list(pair))

def get_string_list_representation(string_list):
    return _get_list_representation(string_list, get_string_representation)

def get_hash_representation(
    hash_,
    key_handler=get_representation,
    value_handler=get_representation,
):
    return '{{{}}}'.format(', '.join([
        '{}: {}'.format(key_handler(key), value_handler(value))
        for key, value in hash_.items()
    ]))

def make_list_from_string(string):
    return list_utilities.reduce_list(string, lambda symbol: float(ord(symbol)))

def make_string_from_list(pair):
    return ''.join(
        list_utilities.map_list(pair, lambda symbol: chr(int(symbol))),
    )

def _get_list_representation(pair, handler):
    return '[{}]'.format(', '.join(list_utilities.map_list(pair, handler)))

def _get_number_representation(number):
    # must not combine a stripping
    return str(number).rstrip('0').rstrip('.')

def _get_pack_representation(pack):
    return '({})'.format(get_representation(pack[0]))

def _get_closure_representation(function):
    return '<closure {:#x}>'.format(id(function))
