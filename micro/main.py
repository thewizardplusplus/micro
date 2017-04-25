import sys
import os

from . import options
from . import builtin_functions
from . import loading
from . import utilities

def main():
    try:
        processed_options = options.process_options()
        filename = processed_options.script
        if filename != '-':
            filename = loading.try_select_path(os.curdir, os.curdir, filename)

        loading.try_load_file(filename, {
            **builtin_functions.BUILTIN_FUNCTIONS,
            **options.make_args_function(processed_options),
        }, processed_options.target, utilities.get_base_path(filename))
    except Exception as exception:
        sys.exit('error: {}'.format(exception))
