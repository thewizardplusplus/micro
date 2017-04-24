import sys

import options
import input_utilities
import lexer
import ast_token
import preparser
import parser
import builtin_functions
import evaluate
import error

processed_options = options.process_options()
code = input_utilities.read_code(processed_options.script)
specific_lexer = lexer.Lexer()
if processed_options.target == 'tokens':
    print(specific_lexer.tokenize(code))

    error.process_errors(
        specific_lexer.get_errors(),
        code,
        options.get_script_name(processed_options.script),
    )
    sys.exit()

specific_preparser = preparser.Preparser(specific_lexer)
preast = specific_preparser.preparse(code)
errors = specific_lexer.get_errors() + specific_preparser.get_errors()
if processed_options.target == 'preast':
    print(preast)

    error.process_errors(
        errors,
        code,
        options.get_script_name(processed_options.script),
    )
    sys.exit()

specific_parser = parser.Parser()
functions = options.add_args_function(
    builtin_functions.BUILTIN_FUNCTIONS,
    processed_options,
)
ast = specific_parser.parse(preast, functions)
errors += specific_parser.get_errors()
if processed_options.target == 'ast':
    print(ast)

    error.process_errors(
        errors,
        code,
        options.get_script_name(processed_options.script),
    )
    sys.exit()

error.process_errors(
    errors,
    code,
    options.get_script_name(processed_options.script),
)
evaluate.evaluate(ast, functions)
