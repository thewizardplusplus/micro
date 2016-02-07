from numbers import Number
from list import list_to_str, str_to_list
from sys import stdout
from function import function
from nil import nil_instance
from math import floor, ceil, trunc
from operator import sub, div
from boolean import boolean

def add(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise TypeError(
            "unsupported operand type(s) for +: '{:s}' and '{:s}'".format(
                type(a).__name__,
                type(b).__name__
            )
        )

    return a + b

def mul(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise TypeError(
            "unsupported operand type(s) for *: '{:s}' and '{:s}'".format(
                type(a).__name__,
                type(b).__name__
            )
        )

    return a * b

def modulo(a, b):
    if (
        not isinstance(a, Number)
        or not float(a).is_integer()
        or not isinstance(b, Number)
        or not float(b).is_integer()
    ):
        raise TypeError(
            "unsupported operand type(s) for %: '{:s}' and '{:s}'".format(
                type(a).__name__,
                type(b).__name__
            )
        )

    return a % b

def print_function(str):
    if not isinstance(str, list):
        raise TypeError(
            "unsupported operand type(s) for print: '{:s}'".format(
                type(str).__name__
            )
        )

    new_str = list_to_str(str)
    stdout.write(new_str)

    return str

def to_string(value):
    return str_to_list(str(value))

def to_number(value):
    if not isinstance(value, list):
        raise TypeError(
            "unsupported operand type(s) for to_num: '{:s}'".format(
                type(value).__name__
            )
        )

    new_value = list_to_str(value)
    return float(new_value)

def while_function(condition, body):
    if not isinstance(condition, function) or not isinstance(body, function):
        raise TypeError(
            "unsupported operand type(s) for while: '{:s}' and '{:s}'".format(
                type(condition).__name__,
                type(body).__name__
            )
        )

    result = nil_instance
    while condition.handle(nil_instance):
        result = body.handle(nil_instance)

    return result

builtin_functions = {
    'nil': function(lambda: nil_instance, arity=0),
    'floor': function(floor, arity=1),
    'ceil': function(ceil, arity=1),
    'trunc': function(trunc, arity=1),
    '+': function(add, arity=2),
    '-': function(sub, arity=2),
    '*': function(mul, arity=2),
    '/': function(div, arity=2),
    '%': function(modulo, arity=2),
    '==': function(lambda a, b: boolean(a == b), arity=2),
    '!=': function(lambda a, b: boolean(a != b), arity=2),
    '<': function(lambda a, b: boolean(float(a) < float(b)), arity=2),
    '<=': function(lambda a, b: boolean(float(a) <= float(b)), arity=2),
    '>': function(lambda a, b: boolean(float(a) > float(b)), arity=2),
    '>=': function(lambda a, b: boolean(float(a) >= float(b)), arity=2),
    'true': function(lambda: boolean(True), arity=0),
    'false': function(lambda: boolean(False), arity=0),
    '&&': function(lambda a, b: a and b, arity=2),
    '||': function(lambda a, b: a or b, arity=2),
    '!': function(lambda a: boolean(not a), arity=1),
    'if': function(lambda condition, a, b: a if condition else b, arity=3),
    '$': function(lambda: [], arity=0),
    ':': function(lambda value, list: [value] + list, arity=2),
    'head': function(lambda list: list[0], arity=1),
    'tail': function(lambda list: list[1:], arity=1),
    'print': function(print_function, arity=1),
    'to_str': function(to_string, arity=1),
    'to_num': function(to_number, arity=1),
    'while': function(while_function, arity=2)
}
