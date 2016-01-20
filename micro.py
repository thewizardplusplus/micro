#!/usr/bin/env python

from sys import argv
from operator import add, sub, mul, div

functions = { \
	'+': (2, add), \
	'-': (2, sub), \
	'*': (2, mul), \
	'/': (2, div) \
}

def get_code():
	return argv[1]

def get_tokens(code):
	return code.split(' ')

if __name__ == '__main__':
	code = get_code()
	tokens = get_tokens(code)
	print(tokens)

	print(functions['+'][1](2, 3))
	print(functions['-'][1](2, 3))
	print(functions['*'][1](2, 3))
	print(functions['/'][1](2, 3))
