CODE = '''
out str + 2 3
'''

if __name__ == '__main__':
    import lexer
    import preparser
    import parser
    import builtin_functions
    import sys
    import evaluate

    specific_lexer = lexer.Lexer()
    specific_preparser = preparser.Preparser(specific_lexer)
    preast = specific_preparser.preparse(CODE)
    specific_parser = parser.Parser()
    ast = specific_parser.parse(preast, builtin_functions.BUILTIN_FUNCTIONS)
    errors = specific_lexer.get_errors() + specific_preparser.get_errors() + specific_parser.get_errors()
    for some_error in errors:
        some_error.detect_position(CODE)
        print(some_error)
    if errors:
        sys.exit()

    evaluate.evaluate(ast, builtin_functions.BUILTIN_FUNCTIONS)
