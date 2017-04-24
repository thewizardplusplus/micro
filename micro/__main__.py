import sys

import options
import builtin_functions
import loading

processed_options = options.process_options()
result, errors = loading.load_file(
    processed_options.script,
    options.add_args_function(
        builtin_functions.BUILTIN_FUNCTIONS,
        processed_options,
    ),
    processed_options.target,
)
if processed_options.target != 'evaluation':
    print(result)

has_errors = False
for error in errors:
    has_errors = True
    sys.stderr.write(str(error) + '\n')
if has_errors:
    sys.exit(1)
