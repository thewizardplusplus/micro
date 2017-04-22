import math
import random
import sys
import datetime

import trampoline
import type_utilities
import string_utilities
import options
import function_type
import list_utilities
import input_utilities
import bitwise_operations
import utilities

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
    'apply': function_type.make_type(
        [2],
        handler=lambda closure, arguments: closure(
            *list_utilities.map_list(arguments),
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
    '_': function_type.make_type([1], handler=lambda x: -x),
    '++': function_type.make_type([1], handler=lambda x: x + 1),
    '+': function_type.make_type([2], handler=lambda x, y: x + y),
    '--': function_type.make_type([1], handler=lambda x: x - 1),
    '-': function_type.make_type([2], handler=lambda x, y: x - y),
    '*': function_type.make_type([2], handler=lambda x, y: x * y),
    '/': function_type.make_type([2], handler=lambda x, y: x / y),
    '%': function_type.make_type([2], handler=lambda x, y: x % y),
    '&': function_type.make_type([2], handler=bitwise_operations.bitwise_and),
    '|': function_type.make_type([2], handler=bitwise_operations.bitwise_or),
    '^': function_type.make_type([2], handler=bitwise_operations.bitwise_xor),
    '<<': function_type.make_type(
        [2],
        handler=bitwise_operations.bitwise_left_shift,
    ),
    '>>': function_type.make_type(
        [2],
        handler=bitwise_operations.bitwise_arithmetic_right_shift,
    ),
    '>>>': function_type.make_type(
        [2],
        handler=bitwise_operations.bitwise_logical_right_shift,
    ),
    '~': function_type.make_type([1], handler=bitwise_operations.bitwise_not),
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
    '[+]': function_type.make_type([2], handler=list_utilities.concatenate),
    'head': function_type.make_type([1], handler=lambda x: x[0]),
    'tail': function_type.make_type([1], handler=lambda x: x[1]),
    '{}': function_type.make_type([], handler=lambda: {}),
    '#': function_type.make_type(
        [3],
        handler=lambda new_key, new_value, hash_: {
            **hash_,
            new_key: new_value,
        } if new_value is not None else {
            key: value
            for key, value in hash_.items()
            if key != new_key
        },
    ),
    '.': function_type.make_type(
        [2],
        handler=lambda key, hash_: hash_.get(key),
    ),
    'keys': function_type.make_type(
        [1],
        handler=lambda hash_: list_utilities.reduce_list(list(hash_.keys())),
    ),
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
    'strh': function_type.make_type(
        [1],
        handler=lambda x: string_utilities.make_list_from_string(
            string_utilities.get_hash_representation(
                x,
                string_utilities.get_string_representation,
            ),
        ),
    ),
    'strhh': function_type.make_type(
        [1],
        handler=lambda x: string_utilities.make_list_from_string(
            string_utilities.get_hash_representation(
                x,
                string_utilities.get_string_representation,
                string_utilities.get_string_representation,
            ),
        ),
    ),
    'env': function_type.make_type(
        [1],
        handler=options.get_environment_variable,
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
_CLOSURE_TRAMPOLINE_WRAPPER = utilities.make_arguments_processor(
    trampoline.closure_trampoline,
)
for name, entity_type in BUILTIN_FUNCTIONS.items():
    if name not in _NOT_TRAMPOLINED_FUNCTIONS and entity_type.arity > 0:
        entity_type.handler = _CLOSURE_TRAMPOLINE_WRAPPER(entity_type.handler)
