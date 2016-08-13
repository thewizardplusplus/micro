import trampoline
import type_utilities
import function_type
import string_utilities
import functools
import math
import random
import sys

@trampoline.make_closure_trampoline_wrapper
def _get_type_name(value):
    name = ''
    if value is None:
        name = 'nil'
    elif isinstance(value, int):
        name = 'int'
    elif isinstance(value, float):
        name = 'num'
    elif type_utilities.is_list(value):
        name = 'list'
    elif type_utilities.is_pack(value):
        name = 'pack'
    # you can't use the function type_utilities.is_closure(), because it's true only for 0-ary functions
    elif isinstance(value, function_type.FunctionType):
        name = 'closure'
    else:
        raise Exception("the unknown type " + value.__class__.__name__)

    return string_utilities.make_list_from_string(name)

@trampoline.make_closure_trampoline_wrapper
def _get_closure_arity(value):
    return functools.reduce(lambda pair, arity: (arity, pair), reversed(value.to_array()), ())

BUILTIN_FUNCTIONS = {
    'nil': function_type.make_type([], handler=lambda: None),
    'num': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: float(string_utilities.make_string_from_list(x)))),
    'type': function_type.make_type([1], handler=_get_type_name),
    'arity': function_type.make_type([1], handler=_get_closure_arity),
    '!': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: not x)),
    '&&': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x and y)),
    '||': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x or y)),
    '==': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x == y)),
    '!=': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x != y)),
    '<': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x < y)),
    '<=': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x <= y)),
    '>': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x > y)),
    '>=': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x >= y)),
    '~': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: -x)),
    '+': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x + y)),
    '-': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x - y)),
    '*': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x * y)),
    '/': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x / y)),
    '%': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: x % y)),
    'floor': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.floor)),
    'ceil': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.ceil)),
    'trunc': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.trunc)),
    'sin': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.sin)),
    'cos': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.cos)),
    'tn': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.tan)),
    'arcsin': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.asin)),
    'arccos': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.acos)),
    'arctn': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.atan)),
    'arctn2': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(math.atan2)),
    'pow': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(math.pow)),
    'sqrt': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.sqrt)),
    'exp': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.exp)),
    'ln': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.log)),
    'lg': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.log10)),
    'abs': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(math.fabs)),
    'random': function_type.make_type([], handler=random.random),
    '$': function_type.make_type([], handler=lambda: ()),
    ',': function_type.make_type([2], handler=trampoline.make_closure_trampoline_wrapper(lambda x, y: (x, y))),
    'head': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: x[0])),
    'tail': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: x[1])),
    'if': function_type.make_type([3], handler=lambda condition, true, false: true if trampoline.closure_trampoline(condition) else false),
    '>@': function_type.make_type([1], handler=lambda value: (value,)),
    '<@': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda value: value[0])),
    '<<@': function_type.make_type([1], handler=trampoline.pack_trampoline),
    'str': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: string_utilities.make_list_from_string(string_utilities.get_representation(x)))),
    'in': function_type.make_type([], handler=lambda: ord(sys.stdin.read(1))),
    'out': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: print(string_utilities.make_string_from_list(x), end=''))),
    'err': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: sys.stderr.write(string_utilities.make_string_from_list(x)))),
    'exit': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: sys.exit(x)))
}

if __name__ == '__main__':
    import read_code
    import lexer
    import preparser
    import parser
    import evaluate

    code = read_code.read_code()
    specific_lexer = lexer.Lexer()
    specific_preparser = preparser.Preparser(specific_lexer)
    preast = specific_preparser.preparse(code)
    specific_parser = parser.Parser()
    ast = specific_parser.parse(preast, BUILTIN_FUNCTIONS)
    result = evaluate.evaluate(ast, BUILTIN_FUNCTIONS)
    print(result)

    for some_error in specific_lexer.get_errors() + specific_preparser.get_errors() + specific_parser.get_errors():
        some_error.detect_position(code)
        print(some_error)
