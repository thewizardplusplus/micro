import argparse

import string_utilities
import list_utilities
import function_type

class HelpFormatter(
    argparse.RawTextHelpFormatter,
    argparse.ArgumentDefaultsHelpFormatter,
):
    pass

def process_options():
    parser = argparse.ArgumentParser(
        prog='micro',
        add_help=False,
        formatter_class=HelpFormatter,
    )

    # optional arguments
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        help='- show the version message and exit',
        version='Micro interpreter, v2.1\n' \
            + 'Copyright (c) 2016, 2017 thewizardplusplus',
    )
    parser.add_argument(
        '-h',
        '--help',
        action='help',
        help='- show the help message and exit',
    )
    parser.add_argument(
        '-t',
        '--target',
        choices=['tokens', 'preast', 'ast', 'evaluation'],
        default='evaluation',
        help='- set a target of a script processing',
    )

    # positional arguments
    parser.add_argument('script', nargs='?', default='-', help='- a script')
    parser.add_argument(
        'args',
        nargs='*',
        default=[],
        help='- script arguments',
    )

    return parser.parse_args()

def add_args_function(functions, options):
    arguments = list_utilities.reduce_list(
        [options.script if options.script != '-' else 'stdin'] + options.args,
        string_utilities.make_list_from_string,
    )
    return {
        **functions.copy(),
        'args': function_type.make_type(
            [],
            handler=lambda: arguments,
        ),
    }
