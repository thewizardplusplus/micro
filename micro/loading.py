import sys
import os

from . import input_utilities
from . import lexer
from . import preparser
from . import parser
from . import evaluate
from . import error
from . import options
from . import function_type
from . import string_utilities
from . import utilities

_SCRIPT_EXTENSION = '.micro'
_LIBRARY_VARIABLE = 'MICRO_LIBRARY'

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
    try:
        result, errors = load_code(code, {
            **functions,
            **_make_load_function(base_path, filename, functions),
        }, target, filename)
        if target != 'evaluation':
            print(result)

        has_errors = False
        for some_error in errors:
            has_errors = True
            sys.stderr.write(str(some_error) + '\n')
        if has_errors:
            sys.exit(1)

        return result
    except error.Error as exception:
        raise error.update_error(exception, code, filename)

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

def try_select_path(base_path, local_base_path, filename):
    if local_base_path is not None:
        full_path = _try_select_file(os.path.join(local_base_path, filename))
        if full_path is not None:
            return full_path

    if base_path is not None:
        full_path = _try_select_file(
            os.path.join(base_path, 'vendor', filename),
        )
        if full_path is not None:
            return full_path

    if os.getenv(_LIBRARY_VARIABLE) is not None:
        full_path = _try_select_file(
            os.path.join(os.getenv(_LIBRARY_VARIABLE), filename),
        )
        if full_path is not None:
            return full_path

    raise Exception('unable to load {}'.format(filename))

def _make_empty_generator():
    return (_ for _ in ())

def _make_load_function(base_path, filename, functions):
    local_base_path = utilities.get_base_path(filename)
    return {
        'load': function_type.make_type(
            [1],
            handler=lambda filename: _load_file(
                base_path,
                local_base_path,
                string_utilities.make_string_from_list(filename),
                functions,
            ),
        ),
    }

def _load_file(base_path, local_base_path, filename, functions, file_cache={}):
    result = None
    filename = os.path.abspath(
        try_select_path(base_path, local_base_path, filename),
    )
    if filename not in file_cache:
        result = try_load_file(filename, functions, base_path=base_path)
        file_cache[filename] = result
    else:
        result = file_cache[filename]

    return result

def _try_select_file(path):
    if os.path.splitext(path)[1] == _SCRIPT_EXTENSION and os.path.isfile(path):
        return path

    full_path = path + _SCRIPT_EXTENSION
    if os.path.isfile(full_path):
        return full_path

    full_path = os.path.join(path, '__main__' + _SCRIPT_EXTENSION)
    if os.path.isfile(full_path):
        return full_path

    return None
