import trampoline
import type_utilities
import string_utilities
import utilities
import math
import function_type
import random
import sys

@trampoline.make_closure_trampoline_wrapper
def _get_type_name(value):
    name = ''
    if value is None:
        name = 'nil'
    elif isinstance(value, float):
        name = 'num'
    elif type_utilities.is_list(value):
        name = 'list'
    elif type_utilities.is_pack(value):
        name = 'pack'
    elif type_utilities.is_closure(value):
        name = 'closure'
    else:
        raise Exception("the unknown type " + value.__class__.__name__)

    return string_utilities.make_list_from_string(name)

BUILTIN_FUNCTIONS = {
    'nil': function_type.make_type([], handler=lambda: None),
    'num': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: float(string_utilities.make_string_from_list(x)))),
    'type': function_type.make_type([1], handler=_get_type_name),
    'arity': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: utilities.reduce_list(list(map(float, x.to_array()))))),
    '!': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: float(not x))),
    '&&': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x and y)),
    '||': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x or y)),
    '==': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: float(x == y))),
    '!=': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: float(x != y))),
    '<': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: float(x < y))),
    '<=': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: float(x <= y))),
    '>': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: float(x > y))),
    '>=': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: float(x >= y))),
    '~': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: -x)),
    '+': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x + y)),
    '-': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x - y)),
    '*': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x * y)),
    '/': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x / y)),
    '%': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x % y)),
    'floor': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: float(math.floor(x)))),
    'ceil': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: float(math.ceil(x)))),
    'trunc': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: float(math.trunc(x)))),
    'round': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: float(round(x)))),
    'sin': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.sin)),
    'cos': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.cos)),
    'tn': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.tan)),
    'arcsin': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.asin)),
    'arccos': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.acos)),
    'arctn': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.atan)),
    'angle': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(math.atan2)),
    'pow': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(math.pow)),
    'sqrt': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.sqrt)),
    'exp': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.exp)),
    'ln': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.log)),
    'lg': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.log10)),
    'abs': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.fabs)),
    'random': function_type.make_type([], handler=random.random),
    '[]': function_type.make_type([], handler=lambda: ()),
    ',': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: (x, y))),
    'head': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: x[0])),
    'tail': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: x[1])),
    'if': function_type.make_type([3], handler=lambda condition, true, false: true if trampoline.closure_trampoline(condition) else false),
    '>@': function_type.make_type([1], handler=lambda value: (value,)),
    '<@': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda value: value[0])),
    '<<@': function_type.make_type([1], handler=trampoline.pack_trampoline),
    'str': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: string_utilities.make_list_from_string(string_utilities.get_representation(x)))),
    'strb': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: string_utilities.make_list_from_string("true" if x else "false"))),
    'strl': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: string_utilities.make_list_from_string(string_utilities.get_string_list_representation(x)))),
    'in': function_type.make_type([], handler=lambda: float(ord(sys.stdin.read(1)))),
    'out': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: print(string_utilities.make_string_from_list(x), end=''))),
    'outln': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: print(string_utilities.make_string_from_list(x)))),
    'err': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: sys.stderr.write(string_utilities.make_string_from_list(x)))),
    'errln': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: sys.stderr.write(string_utilities.make_string_from_list(x) + '\n'))),
    'exit': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: sys.exit(int(x)))),
}
