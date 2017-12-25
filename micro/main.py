import sys
import os

from . import options
from . import builtin_functions
from . import loading
from . import utilities
from . import error
from . import file_selection
from . import file_cache

def main():
    try:
        options.initialize_environment_variables()

        processed_options = options.process_options()
        filename = processed_options.script
        if filename != '-':
            filename = file_selection.try_select_path(
                os.curdir,
                os.curdir,
                filename,
            )

        specific_file_cache = file_cache.FileCache()
        loading.load_file(
            filename,
            {
                **builtin_functions.BUILTIN_FUNCTIONS,
                **options.make_args_function(processed_options),
            },
            processed_options.target,
            utilities.get_base_path(filename),
            specific_file_cache,
        )
    except Exception as exception:
        sys.exit('error: ' + str(exception))
    except KeyboardInterrupt:
        # output a line break after the ^C symbol in a terminal
        print('')

        sys.exit(1)
