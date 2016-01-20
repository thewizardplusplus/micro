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

def evaluate(tokens):
	name = tokens[0]
	if name not in functions:
		return int(name), 1

	function = functions[name]
	arguments = []
	offset = 1
	for _ in xrange(function[0]):
		value, shift = evaluate(tokens[offset:])
		arguments.append(value)
		offset += shift

	value = function[1](*arguments)
	return value, 1 + len(arguments)

if __name__ == '__main__':
	code = get_code()
	tokens = get_tokens(code)
	value, _ = evaluate(tokens)
	print(value)
