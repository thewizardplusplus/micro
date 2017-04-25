import options
import builtin_functions
import loading
import utilities

processed_options = options.process_options()
loading.try_load_file(
    processed_options.script,
    {
        **builtin_functions.BUILTIN_FUNCTIONS,
        **options.make_args_function(processed_options),
    },
    processed_options.target,
    utilities.get_base_path(processed_options.script),
)
