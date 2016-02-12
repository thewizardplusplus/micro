from numbers import Number
from list import list_to_str, str_to_list
from sys import stdout
from function import function
from nil import nil_instance
import math
from operator import sub, div
from boolean import boolean
import evaluate_list

def neg(a):
    if not isinstance(a, Number):
        raise TypeError(
            "unsupported operand type(s) for #: '{:s}'".format(
                type(a).__name__
            )
        )

    return -a

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

def eval_function(str):
    str = list_to_str(str)
    return evaluate_list.evaluate_string(str)

builtin_functions = {
    'nil': function(lambda: nil_instance, arity=0),
    'floor': function(math.floor, arity=1),
    'ceil': function(math.ceil, arity=1),
    'trunc': function(math.trunc, arity=1),
    '#': function(neg, arity=1),
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
    'sin': function(lambda a: math.sin(float(a)), arity=1),
    'cos': function(lambda a: math.cos(float(a)), arity=1),
    'tn': function(lambda a: math.tan(float(a)), arity=1),
    'arcsin': function(lambda a: math.asin(float(a)), arity=1),
    'arccos': function(lambda a: math.acos(float(a)), arity=1),
    'arctn': function(lambda a: math.atan(float(a)), arity=1),
    'arctn2': function(lambda a, b: math.atan2(float(a), float(b)), arity=2),
    'sh': function(lambda a: math.sinh(float(a)), arity=1),
    'ch': function(lambda a: math.cosh(float(a)), arity=1),
    'th': function(lambda a: math.tanh(float(a)), arity=1),
    'sqrt': function(lambda a: math.sqrt(float(a)), arity=1),
    'pow': function(lambda a, b: math.pow(float(a), float(b)), arity=2),
    'exp': function(lambda a: math.exp(float(a)), arity=1),
    'ln': function(lambda a: math.log(float(a)), arity=1),
    'lg': function(lambda a: math.log10(float(a)), arity=1),
    'abs': function(lambda a: math.fabs(float(a)), arity=1),
    'true': function(lambda: boolean(True), arity=0),
    'false': function(lambda: boolean(False), arity=0),
    '&&': function(lambda a, b: a and b, arity=2),
    '||': function(lambda a, b: a or b, arity=2),
    '!': function(lambda a: boolean(not a), arity=1),
    'if': function(lambda condition, a, b: a if condition else b, arity=3),
    '$': function(lambda: [], arity=0),
    ':': function(lambda value, list: [value] + list, arity=2),
    'list': function(
        lambda number, value: [value for _ in xrange(number)],
        arity=2
    ),
    'append': function(lambda list, item: list + [item], arity=2),
    'concat': function(lambda list_1, list_2: list_1 + list_2, arity=2),
    'item': function(lambda list, index: list[index], arity=2),
    'len': function(lambda list: len(list), arity=1),
    'print': function(print_function, arity=1),
    'to_str': function(to_string, arity=1),
    'to_num': function(to_number, arity=1),
    'while': function(while_function, arity=2),
    'eval': function(eval_function, arity=1)
}
