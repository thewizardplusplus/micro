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
            return ord(self._remove_quotes(entity.value))
        elif entity.name == 'STRING':
            return self._remove_quotes(entity.value)
        elif entity.name == 'IDENTIFIER':
            return functions[entity.value]()
        elif entity.name == 'function':
            raise Exception("not yet implement")
        elif entity.name == 'call':
            raise Exception("not yet implement")

    def _remove_quotes(self, string):
        return string[1:-1]

    def _evaluate_call(self, call):
        return 12

if __name__ == '__main__':
    import function_type
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
