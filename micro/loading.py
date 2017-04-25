import sys

import input_utilities
import lexer
import preparser
import parser
import evaluate
import error
import options
import function_type
import string_utilities

def load_code(code, functions={}, target='evaluation', filename=None):
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

    return evaluate.evaluate(ast, functions), _make_empty_generator()

def try_load_code(
    code,
    functions={},
    target='evaluation',
    filename=None,
    base_path=None,
):
    result, errors = load_code(code, {
        **functions,
        **_make_load_function(base_path, filename, functions),
    }, target, filename)
    if target != 'evaluation':
        print(result)

    has_errors = False
    for error in errors:
        has_errors = True
        sys.stderr.write(str(error) + '\n')
    if has_errors:
        sys.exit(1)

    return result

def try_load_file(
    filename='-',
    functions={},
    target='evaluation',
    base_path=None,
):
    return try_load_code(
        input_utilities.read_code(filename),
        functions,
        target,
        filename,
        base_path,
    )

def _make_empty_generator():
    return (_ for _ in ())

def _make_load_function(base_path, filename, functions):
    local_filename = filename
    return {
        'load': function_type.make_type(
            [1],
            handler=lambda filename: string_utilities.make_list_from_string(
                str({
                    "local_filename": local_filename,
                    "filename": string_utilities.make_string_from_list(
                        filename,
                    ),
                }),
            ),
        ),
    }
