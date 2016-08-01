import function_type
import math
import random

def _trampoline(value):
    while hasattr(value, '__call__'):
        value = value()

    return value

BUILTIN_FUNCTIONS = {
    '!': function_type.make_type([1], handler=lambda x: not x),
    '&&': function_type.make_type([2], handler=lambda x, y: x and y),
    '||': function_type.make_type([2], handler=lambda x, y: x or y),
    '==': function_type.make_type([2], handler=lambda x, y: x == y),
    '!=': function_type.make_type([2], handler=lambda x, y: x != y),
    '<': function_type.make_type([2], handler=lambda x, y: x < y),
    '<=': function_type.make_type([2], handler=lambda x, y: x <= y),
    '>': function_type.make_type([2], handler=lambda x, y: x > y),
    '>=': function_type.make_type([2], handler=lambda x, y: x >= y),
    '~': function_type.make_type([1], handler=lambda x: -x),
    '+': function_type.make_type([2], handler=lambda x, y: x + y),
    '-': function_type.make_type([2], handler=lambda x, y: x - y),
    '*': function_type.make_type([2], handler=lambda x, y: x * y),
    '/': function_type.make_type([2], handler=lambda x, y: x / y),
    '%': function_type.make_type([2], handler=lambda x, y: x % y),
    'floor': function_type.make_type([1], handler=lambda x: math.floor(x)),
    'ceil': function_type.make_type([1], handler=lambda x: math.ceil(x)),
    'random': function_type.make_type([], handler=lambda: random.random()),
    '$': function_type.make_type([], handler=lambda: ()),
    ',': function_type.make_type([2], handler=lambda x, y: (x, y)),
    'head': function_type.make_type([1], handler=lambda x: x[0]),
    'tail': function_type.make_type([1], handler=lambda x: x[1]),
    'if': function_type.make_type([3], handler=lambda condition, true, false: true if condition else false),
    '@': function_type.make_type([1], handler=_trampoline),
    'out': function_type.make_type([1], handler=lambda x: print(x) or x)
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
