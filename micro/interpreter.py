import utilities
import function_type

class Interpreter:
    _errors = []

    def evaluate(self, ast, functions={}):
        result = None
        for entity in ast.children:
            result = self._evaluate_entity(entity, functions)

        return result

    def get_errors(self):
        return self._errors

    def _evaluate_entity(self, entity, functions):
        if entity.name == 'INTEGRAL_NUMBER':
            return int(entity.value)
        elif entity.name == 'REAL_NUMBER':
            return float(entity.value)
        elif entity.name == 'CHARACTER':
            return ord(_remove_quotes(entity.value))
        elif entity.name == 'STRING':
            return _remove_quotes(entity.value)
        elif entity.name == 'IDENTIFIER':
            function = functions[entity.value]
            if function.arity > 0:
                return function
            else:
                return function()
        elif entity.name == 'function':
            return self._evaluate_function(entity, functions)
        elif entity.name == 'call':
            return self._evaluate_call(entity, functions)

    def _evaluate_function(self, entity, functions):
        name, entity_type = utilities.extract_function(entity)
        if name != '':
            functions[name] = entity_type

        handler = self._make_handler(entity, functions.copy())
        entity_type.set_handler(handler)

        return handler

    def _make_handler(self, function_node, functions):
        def _function_handler(*args):
            parameters = args
            for index, argument in enumerate(function_node.children[0].children[1].children):
                entity_type = function_type.make_type(argument.children[1])
                functions[argument.children[0].value] = entity_type

                parameter = parameters[index]
                def _argument_handler(*args, arity=entity_type.arity, parameter=parameter):
                    if arity > 0:
                        return parameter(*args)
                    else:
                        return parameter

                entity_type.set_handler(_argument_handler)

            return self.evaluate(function_node.children[1], functions)

        return _function_handler

    def _evaluate_call(self, call, functions):
        inner_function = self._evaluate_entity(call.children[0].children[0].children[0], functions)
        parameters = [self._evaluate_entity(parameter, functions) for parameter in call.children[1].children]
        return inner_function(*parameters)

def _remove_quotes(string):
    return string[1:-1]

if __name__ == '__main__':
    import read_code
    import lexer
    import preparser
    import parser

    FUNCTIONS = {
        'ans': function_type.make_type([], handler=lambda: 42),
        '~': function_type.make_type([1], handler=lambda x: -x),
        '+': function_type.make_type([2], handler=lambda x, y: x + y),
        '-': function_type.make_type([2], handler=lambda x, y: x - y),
        '*': function_type.make_type([2], handler=lambda x, y: x * y),
        '/': function_type.make_type([2], handler=lambda x, y: x / y),
        '%': function_type.make_type([2], handler=lambda x, y: x % y)
    }

    code = read_code.read_code()
    specific_lexer = lexer.Lexer()
    specific_preparser = preparser.Preparser(specific_lexer)
    preast = specific_preparser.preparse(code)
    specific_parser = parser.Parser()
    ast = specific_parser.parse(preast, FUNCTIONS)
    print(ast)
    interpreter = Interpreter()
    result = interpreter.evaluate(ast, FUNCTIONS)
    print(result)

    for some_error in specific_lexer.get_errors() + specific_preparser.get_errors() + specific_parser.get_errors() + interpreter.get_errors():
        some_error.detect_position(code)
        print(some_error)
