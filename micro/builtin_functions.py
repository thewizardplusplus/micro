import trampoline
import function_type
import math
import random
import string_utilities

BUILTIN_FUNCTIONS = {
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
    'out': function_type.make_type([1], handler=trampoline.make_closure_trampoline_wrapper(lambda x: print(string_utilities.make_string_from_list(x), end='')))
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
