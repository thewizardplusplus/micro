import sys

from . import options
from . import builtin_functions
from . import loading

def main():
    try:
        options.initialize_environment_variables()

        processed_options = options.process_options()
        loading.load_main_file(processed_options.script, {
            **builtin_functions.BUILTIN_FUNCTIONS,
            **options.make_args_function(processed_options),
        }, processed_options.target)
    except Exception as exception:
        sys.exit('error: ' + str(exception))
    except KeyboardInterrupt:
        # output a line break after the ^C symbol in a terminal
        print('')

        sys.exit(1)
