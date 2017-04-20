import math
import random
import sys
import datetime

import trampoline
import type_utilities
import string_utilities
import utilities
import function_type
import list_utilities
import input_utilities

BUILTIN_FUNCTIONS = {
    'nil': function_type.make_type([], handler=lambda: None),
    'false': function_type.make_type([], handler=lambda: 0.0),
    'true': function_type.make_type([], handler=lambda: 1.0),
    'num': function_type.make_type(
        [1],
        handler=lambda x: float(string_utilities.make_string_from_list(x)),
    ),
    'type': function_type.make_type(
        [1],
        handler=lambda x: string_utilities.make_list_from_string(
            type_utilities.get_type_name(x),
        ),
    ),
    'arity': function_type.make_type(
        [1],
        handler=lambda x: list_utilities.reduce_list(
            list(map(float, x.to_array())),
        ),
    ),
    '!': function_type.make_type([1], handler=lambda x: float(not x)),
    '&&': function_type.make_type([2], handler=lambda x, y: x and y),
    '||': function_type.make_type([2], handler=lambda x, y: x or y),
    '==': function_type.make_type([2], handler=lambda x, y: float(x == y)),
    '!=': function_type.make_type([2], handler=lambda x, y: float(x != y)),
    '<': function_type.make_type([2], handler=lambda x, y: float(x < y)),
    '<=': function_type.make_type([2], handler=lambda x, y: float(x <= y)),
    '>': function_type.make_type([2], handler=lambda x, y: float(x > y)),
    '>=': function_type.make_type([2], handler=lambda x, y: float(x >= y)),
    '~': function_type.make_type([1], handler=lambda x: -x),
    '+': function_type.make_type([2], handler=lambda x, y: x + y),
    '-': function_type.make_type([2], handler=lambda x, y: x - y),
    '*': function_type.make_type([2], handler=lambda x, y: x * y),
    '/': function_type.make_type([2], handler=lambda x, y: x / y),
    '%': function_type.make_type([2], handler=lambda x, y: x % y),
    'floor': function_type.make_type(
        [1],
        handler=lambda x: float(math.floor(x)),
    ),
    'ceil': function_type.make_type([1], handler=lambda x: float(math.ceil(x))),
    'trunc': function_type.make_type(
        [1],
        handler=lambda x: float(math.trunc(x)),
    ),
    'round': function_type.make_type([1], handler=lambda x: float(round(x))),
    'sin': function_type.make_type([1], handler=math.sin),
    'cos': function_type.make_type([1], handler=math.cos),
    'tn': function_type.make_type([1], handler=math.tan),
    'arcsin': function_type.make_type([1], handler=math.asin),
    'arccos': function_type.make_type([1], handler=math.acos),
    'arctn': function_type.make_type([1], handler=math.atan),
    'angle': function_type.make_type([2], handler=math.atan2),
    'pow': function_type.make_type([2], handler=math.pow),
    'sqrt': function_type.make_type([1], handler=math.sqrt),
    'exp': function_type.make_type([1], handler=math.exp),
    'ln': function_type.make_type([1], handler=math.log),
    'lg': function_type.make_type([1], handler=math.log10),
    'abs': function_type.make_type([1], handler=math.fabs),
    'random': function_type.make_type([], handler=random.random),
    '[]': function_type.make_type([], handler=lambda: ()),
    ',': function_type.make_type([2], handler=lambda x, y: (x, y)),
    'head': function_type.make_type([1], handler=lambda x: x[0]),
    'tail': function_type.make_type([1], handler=lambda x: x[1]),
    'if': function_type.make_type(
        [3],
        handler=lambda condition, true, false: \
            true if trampoline.closure_trampoline(condition) else false,
    ),
    '>@': function_type.make_type([1], handler=lambda value: (value,)),
    '<@': function_type.make_type([1], handler=lambda value: value[0]),
    '<<@': function_type.make_type([1], handler=trampoline.pack_trampoline),
    'str': function_type.make_type(
        [1],
        handler=lambda x: string_utilities.make_list_from_string(
            string_utilities.get_representation(x),
        ),
    ),
    'strb': function_type.make_type(
        [1],
        handler=lambda x: string_utilities.make_list_from_string(
            'true' if x else 'false',
        ),
    ),
    'strl': function_type.make_type(
        [1],
        handler=lambda x: string_utilities.make_list_from_string(
            string_utilities.get_string_list_representation(x),
        ),
    ),
    'env': function_type.make_type(
        [1],
        handler=utilities.get_environment_variable,
    ),
    'time': function_type.make_type(
        [],
        handler=lambda: \
            datetime.datetime.now(datetime.timezone.utc).timestamp(),
    ),
    'in': function_type.make_type([1], handler=input_utilities.read_input),
    'out': function_type.make_type(
        [1],
        handler=lambda x: print(
            string_utilities.make_string_from_list(x),
            end='',
        ),
    ),
    'outln': function_type.make_type(
        [1],
        handler=lambda x: print(string_utilities.make_string_from_list(x)),
    ),
    'err': function_type.make_type(
        [1],
        handler=lambda x: sys.stderr.write(
            string_utilities.make_string_from_list(x),
        ),
    ),
    'errln': function_type.make_type(
        [1],
        handler=lambda x: sys.stderr.write(
            string_utilities.make_string_from_list(x) + '\n',
        ),
    ),
    'exit': function_type.make_type([1], handler=lambda x: sys.exit(int(x))),
}
_NOT_TRAMPOLINED_FUNCTIONS = ['if', '>@']
for name, entity_type in BUILTIN_FUNCTIONS.items():
    if name not in _NOT_TRAMPOLINED_FUNCTIONS and entity_type.arity > 0:
        entity_type.handler = trampoline.make_closure_trampoline_wrapper(
            entity_type.handler,
        )
