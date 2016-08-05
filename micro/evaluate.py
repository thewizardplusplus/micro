import utilities
import string_utilities
import function_type

def evaluate(ast, functions={}, required_unpacking=True):
    result = None
    for entity in ast.children:
        result = _evaluate_entity(entity, functions, required_unpacking)

    return result

def make_unpacking_wrapper(handler):
    return lambda *args: handler(*[_unpack(arg, True) for arg in args])

def _evaluate_entity(entity, functions, required_unpacking):
    if entity.name == 'INTEGRAL_NUMBER':
        return int(entity.value)
    elif entity.name == 'REAL_NUMBER':
        return float(entity.value)
    elif entity.name == 'CHARACTER':
        return ord(utilities.unquote(entity.value))
    elif entity.name == 'STRING':
        return string_utilities.string_to_list(utilities.unquote(entity.value))
    elif entity.name == 'IDENTIFIER':
        return _unpack(functions[entity.value], required_unpacking)
    elif entity.name == 'function':
        return _evaluate_function(entity, functions)
    elif entity.name == 'call':
        return _evaluate_call(entity, functions, required_unpacking)

def _unpack(value, required_unpacking):
    if not required_unpacking or (isinstance(value, function_type.FunctionType) and value.is_callable()):
        return value
    else:
        return _trampoline(value)

def _trampoline(value):
    while hasattr(value, '__call__'):
        value = value()

    return value

def _evaluate_function(entity, functions):
    name, entity_type = utilities.extract_function(entity)
    if name != '':
        functions[name] = entity_type

    handler = _make_function_handler(entity, functions.copy())
    entity_type.set_handler(handler)

    return entity_type

def _make_function_handler(function_node, functions):
    def handler(*args):
        for i, argument in enumerate(function_node.children[0].children[1].children):
            entity_type = function_type.make_type(argument.children[1])
            entity_type.set_handler(args[i] if entity_type.arity > 0 else lambda value=args[i]: value)

            functions[argument.children[0].value] = entity_type

        return evaluate(function_node.children[1], functions, False)

    return handler

def _evaluate_call(call, functions, required_unpacking):
    inner_function = _evaluate_entity(call.children[0].children[0].children[0], functions, False)
    parameters = [_evaluate_entity(parameter, functions, False) for parameter in call.children[1].children]
    return _unpack(inner_function(*parameters), required_unpacking)

if __name__ == '__main__':
    import read_code
    import lexer
    import preparser
    import parser

    FUNCTIONS = {
        'ans': function_type.make_type([], handler=lambda: 42),
        '~': function_type.make_type([1], handler=make_unpacking_wrapper(lambda x: -x)),
        '+': function_type.make_type([2], handler=make_unpacking_wrapper(lambda x, y: x + y)),
        '-': function_type.make_type([2], handler=make_unpacking_wrapper(lambda x, y: x - y)),
        '*': function_type.make_type([2], handler=make_unpacking_wrapper(lambda x, y: x * y)),
        '/': function_type.make_type([2], handler=make_unpacking_wrapper(lambda x, y: x / y)),
        '%': function_type.make_type([2], handler=make_unpacking_wrapper(lambda x, y: x % y))
    }

    code = read_code.read_code()
    specific_lexer = lexer.Lexer()
    specific_preparser = preparser.Preparser(specific_lexer)
    preast = specific_preparser.preparse(code)
    specific_parser = parser.Parser()
    ast = specific_parser.parse(preast, FUNCTIONS)
    print(ast)
    result = evaluate(ast, FUNCTIONS)
    print(result)

    for some_error in specific_lexer.get_errors() + specific_preparser.get_errors() + specific_parser.get_errors():
        some_error.detect_position(code)
        print(some_error)
