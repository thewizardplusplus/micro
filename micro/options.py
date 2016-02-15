import argparse

def parse_options():
    parser = make_options_parser()
    return parser.parse_args()

def make_options_parser():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        help='- show a version message and exit;',
        version='Micro interpreter, v1.0 (Copyright (c) 2016 thewizardplusplus)'
    )
    parser.add_argument(
        '-h',
        '--help',
        action='help',
        help='- show a help message and exit;'
    )
    parser.add_argument(
        '-i',
        '--input',
        action='store_true',
        help='- read a code from stdin;'
    )
    parser.add_argument(
        '-c',
        '--code',
        help='- evaluate the code at a beginning;'
    )
    parser.add_argument(
        '-t',
        '--tokens',
        action='store_true',
        help='- show tokens and exit;'
    )
    parser.add_argument(
        '-p',
        '--print',
        action='store_true',
        help='- print a result before an exit.'
    )

    parser.add_argument('file', nargs='?', help='- an input file;')
    parser.add_argument('args', nargs='*', help='- script arguments.')

    return parser
