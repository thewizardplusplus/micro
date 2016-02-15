from __future__ import print_function
from lexer import read_stdin, read_file, remove_comments, tokenize
from options import parse_options
from builtin_functions import get_builtin_functions
from evaluate_list import evaluate_list

def run():
    options = parse_options()
    code = get_code(options)
    code = remove_comments(code)
    tokens = tokenize(code)
    if options.tokens:
        print(tokens)
        exit(0)

    builtin_functions = get_builtin_functions(options.args)
    result, _ = evaluate_list(tokens, builtin_functions)
    if getattr(options, 'print'):
        print(result)

def run_safe():
    try:
        run()
    except Exception as exception:
        print('Error: {!s}.'.format(exception))

def get_code(options):
    all_code = ''
    if options.code is not None:
        all_code = options.code

    if options.input:
        code = read_stdin()
        all_code += ' ' + code
    elif options.file is not None:
        code = read_file(options.file)
        all_code += ' ' + code
    elif not all_code:
        raise Exception('should be specified a source of a code')

    return all_code
