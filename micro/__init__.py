#!/usr/bin/env python

from lexer import read_code
from evaluate_list import evaluate_string

if __name__ == '__main__':
    try:
        code = read_code()
        evaluate_string(code)
    except Exception as exception:
        print('Error: {!s}.'.format(exception))
