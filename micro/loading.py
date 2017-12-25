import sys
import os

from . import input_utilities
from . import evaluate
from . import error
from . import function_type
from . import string_utilities
from . import utilities
from . import file_selection
from . import file_cache
from . import builtin_functions

class FileLoader(file_cache.BaseFileLoader):
    def __init__(self, file_cache):
        self._file_cache = file_cache

    def make_file_id(self, base_path, local_base_path, filename):
        return os.path.abspath(file_selection.try_select_path(
            base_path,
            local_base_path,
            filename,
        ))

    def load_file(
        self,
        base_path,
        local_base_path,
        filename,
        file_id,
        functions={},
    ):
        return load_file(
            file_id,
            functions,
            base_path=base_path,
            file_cache=self._file_cache,
        )

def load_code(
    code,
    functions={},
    target='evaluation',
    filename=None,
    is_main_file=False,
    base_path=None,
    file_cache=None,
):
    result, errors = evaluate.evaluate_code(code, {
        **functions,
        **_make_load_function(file_cache, base_path, filename, functions),
        **_make_is_main_function(is_main_file),
    }, target)
    if target != 'evaluation':
        print(result)

    has_errors = False
    for some_error in errors:
        has_errors = True

        some_error = error.update_error(some_error, code, filename)
        sys.stderr.write(str(some_error) + '\n')
    if has_errors:
        sys.exit(1)

    return result

def load_file(
    filename='-',
    functions={},
    target='evaluation',
    is_main_file=False,
    base_path=None,
    file_cache=None,
):
    return load_code(
        input_utilities.read_code(filename),
        functions,
        target,
        filename,
        is_main_file,
        base_path,
        file_cache,
    )

def _default_load_function(filename):
    raise Exception("the load function isn't available")

def _make_load_function(file_cache, base_path, filename, functions):
    if file_cache is not None:
        local_base_path = utilities.get_base_path(filename)
        load_function = lambda filename: file_cache.get_file(
            base_path,
            local_base_path,
            string_utilities.make_string_from_list(filename),
            functions,
        )
    else:
        load_function = _default_load_function

    return {'load': function_type.make_type(
        [1],
        handler=builtin_functions.CLOSURE_TRAMPOLINE_WRAPPER(load_function),
    )}

def _make_is_main_function(is_main_file):
    return {'is_main': function_type.make_type(
        [],
        handler=lambda: is_main_file,
    )}
