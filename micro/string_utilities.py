import json

import type_utilities
import list_utilities

def quote(string):
    return json.dumps(string)

def unquote(string):
    # force a wrapping of a string to double quotes
    string = '"{}"'.format(string[1:-1])
    return json.loads(string)

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
        raise Exception('the unknown type {}'.format(value.__class__.__name__))

    return representation

def get_string_list_representation(string_list):
    return _get_list_representation(
        string_list,
        lambda item: quote(make_string_from_list(item)),
    )

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
