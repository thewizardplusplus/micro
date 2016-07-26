class Interpreter:
    _errors = []

    def __init__(self, functions={}):
        self._functions = functions

    def evaluate(self, ast):
        result = None
        for call in ast.children:
            result = self._evaluate_call(call)

        return result

    def get_errors(self):
        return self._errors

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
