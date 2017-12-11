import argparse
import os

import dotenv

from . import string_utilities
from . import list_utilities
from . import function_type
from . import utilities

class HelpFormatter(
    argparse.RawTextHelpFormatter,
    argparse.ArgumentDefaultsHelpFormatter,
):
    pass

def process_options():
    parser = argparse.ArgumentParser(
        prog=__package__,
        add_help=False,
        formatter_class=HelpFormatter,
    )

    # optional arguments
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        help='- show the version message and exit',
        version='Micro interpreter, v{}\n'.format(utilities.MICRO_VERSION) \
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

def get_script_name(filename):
    return filename if filename != '-' else 'stdin'

def make_args_function(options):
    arguments = list_utilities.reduce_list(
        [get_script_name(options.script)] + options.args,
        string_utilities.make_list_from_string,
    )
    return {
        'args': function_type.make_type(
            [],
            handler=lambda: arguments,
        ),
    }

def initialize_environment_variables():
    dotenv.load_dotenv(dotenv.find_dotenv(usecwd=True))

def get_environment_variable(name):
    value = os.getenv(string_utilities.make_string_from_list(name))
    if value is None:
        return None

    return string_utilities.make_list_from_string(value)
