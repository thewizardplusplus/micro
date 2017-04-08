import help_formatter
import argparse

def process_options():
    parser = _make_options_parser()
    return parser.parse_args()

def _make_options_parser():
    parser = argparse.ArgumentParser(
        prog='micro',
        add_help=False,
        formatter_class=help_formatter.HelpFormatter
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        help='- show the version message and exit',
        version='Micro interpreter, v2.1\nCopyright (c) 2016, 2017 thewizardplusplus'
    )
    parser.add_argument(
        '-h',
        '--help',
        action='help',
        help='- show the help message and exit'
    )
    parser.add_argument(
        '-t',
        '--target',
        choices=['tokens', 'preast', 'ast', 'evaluation'],
        default='evaluation',
        help='- set a target of a script processing'
    )

    parser.add_argument('script', nargs='?', default='-', help='- a script')
    parser.add_argument(
        'args',
        nargs='*',
        default=[],
        help='- script arguments'
    )

    return parser

if __name__ == '__main__':
    options = process_options()
    print(options)
