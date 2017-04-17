import sys
import options
import read_code
import lexer
import ast_token
import json
import preparser
import parser
import builtin_functions
import evaluate

def _process_errors(errors, code):
    for some_error in errors:
        some_error.detect_position(code)
        sys.stderr.write(str(some_error) + '\n')

processed_options = options.process_options()
code = read_code.read_code(processed_options.script)
specific_lexer = lexer.Lexer()
if processed_options.target == 'tokens':
    tokens = specific_lexer.tokenize(code)
    _process_errors(specific_lexer.get_errors(), code)

    print(json.dumps(tokens, cls=ast_token.AstTokenEncoder))
    sys.exit(1 if specific_lexer.get_errors() else 0)

specific_preparser = preparser.Preparser(specific_lexer)
preast = specific_preparser.preparse(code)
errors = specific_lexer.get_errors() + specific_preparser.get_errors()
if processed_options.target == 'preast':
    _process_errors(errors, code)

    print(preast)
    sys.exit(1 if errors else 0)

specific_parser = parser.Parser()
functions = options.add_args_function(builtin_functions.BUILTIN_FUNCTIONS, processed_options)
ast = specific_parser.parse(preast, functions)
errors += specific_parser.get_errors()
if processed_options.target == 'ast':
    _process_errors(errors, code)

    print(ast)
    sys.exit(1 if errors else 0)

_process_errors(errors, code)
if errors:
    sys.exit(1)

evaluate.evaluate(ast, functions)
