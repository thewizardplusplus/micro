import input_utilities
import lexer
import preparser
import parser
import evaluate
import error
import options

def load_file(filename='-', functions={}, target='evaluation'):
    code = input_utilities.read_code(filename)
    specific_lexer = lexer.Lexer()
    if target == 'tokens':
        return specific_lexer.tokenize(code), error.update_errors(
            specific_lexer.get_errors(),
            code,
            filename,
        )

    specific_preparser = preparser.Preparser(specific_lexer)
    preast = specific_preparser.preparse(code)
    errors = specific_lexer.get_errors() + specific_preparser.get_errors()
    if target == 'preast':
        return preast, error.update_errors(errors, code, filename)

    specific_parser = parser.Parser()
    ast = specific_parser.parse(preast, functions)
    errors += specific_parser.get_errors()
    if target == 'ast' or len(errors) != 0:
        return ast, error.update_errors(errors, code, filename)

    return evaluate.evaluate(ast, functions), (_ for _ in ())
