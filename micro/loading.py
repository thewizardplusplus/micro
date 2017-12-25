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

class FileLoader(file_cache.BaseFileLoader):
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
        return try_load_file(file_id, functions, base_path=base_path)

def try_load_code(
    code,
    functions={},
    target='evaluation',
    filename=None,
    base_path=None,
):
    result, errors = evaluate.evaluate_code(code, {
        **functions,
        **_make_load_function(base_path, filename, functions),
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
    filename = os.path.abspath(file_selection.try_select_path(
        base_path,
        local_base_path,
        filename,
    ))
    if filename not in file_cache:
        result = try_load_file(filename, functions, base_path=base_path)
        file_cache[filename] = result
    else:
        result = file_cache[filename]

    return result
