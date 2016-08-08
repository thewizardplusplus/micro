import read_code
import lexer
import preparser
import parser
import builtin_functions
import sys
import evaluate

code = read_code.read_code()
specific_lexer = lexer.Lexer()
specific_preparser = preparser.Preparser(specific_lexer)
preast = specific_preparser.preparse(code)
specific_parser = parser.Parser()
ast = specific_parser.parse(preast, builtin_functions.BUILTIN_FUNCTIONS)
errors = specific_lexer.get_errors() + specific_preparser.get_errors() + specific_parser.get_errors()
for some_error in errors:
    some_error.detect_position(code)
    sys.stderr.write(str(some_error) + '\n')
if errors:
    sys.exit(1)

evaluate.evaluate(ast, builtin_functions.BUILTIN_FUNCTIONS)
