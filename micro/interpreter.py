class Interpreter:
    _errors = []

    def __init__(self, functions={}):
        self._functions = functions

    def evaluate(self, ast):
        result = None
        for entity in ast.children:
            result = self._evaluate_entity(entity)

        return result

    def get_errors(self):
        return self._errors

    def _evaluate_entity(self, entity):
        if entity.name == 'INTEGRAL_NUMBER':
            return int(entity.value)
        elif entity.name == 'REAL_NUMBER':
            return float(entity.value)
        elif entity.name == 'CHARACTER':
            return ord(self._remove_quotes(entity.value))
        elif entity.name == 'STRING':
            return self._remove_quotes(entity.value)
        elif entity.name == 'IDENTIFIER':
            raise Exception("not yet implement")
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

    FUNCTIONS_FOR_PARSER = {
        '@': function_type.make_type([]),
        '~': function_type.make_type([1]),
        '+': function_type.make_type([2]),
        'rand': function_type.make_type([1, 1, 1]),
        'range': function_type.make_type([0, 2])
    }
    FUNCTIONS_FOR_INTERPRETER = {
        '~': lambda x: -x,
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }

    code = read_code.read_code()
    specific_lexer = lexer.Lexer()
    specific_preparser = preparser.Preparser(specific_lexer)
    preast = specific_preparser.preparse(code)
    specific_parser = parser.Parser(FUNCTIONS_FOR_PARSER)
    ast = specific_parser.parse(preast)
    interpreter = Interpreter(FUNCTIONS_FOR_INTERPRETER)
    result = interpreter.evaluate(ast)
    print(result)

    for some_error in specific_lexer.get_errors() + specific_preparser.get_errors() + specific_parser.get_errors() + interpreter.get_errors():
        some_error.detect_position(code)
        print(some_error)
