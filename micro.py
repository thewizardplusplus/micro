#!/usr/bin/env python

from sys import argv
from operator import add, sub, mul, div
from uuid import uuid4

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

def generate_name():
	return str(uuid4())

def parse_function(tokens):
	name = ''
	if tokens[0] != '(':
		name = tokens[0]
		tokens = tokens[1:]
	else:
		name = generate_name()
	# cut the open parenthesis
	tokens = tokens[1:]

	return name, (23, None), tokens[-1:]

def evaluate(tokens):
	name = tokens[0]
	tokens = tokens[1:]
	if name == 'fn':
		name, function, tokens = parse_function(tokens)
		functions[name] = function

		return 0, tokens
	if name not in functions:
		return int(name), tokens

	function = functions[name]
	arguments = []
	for _ in xrange(function[0]):
		value, tokens = evaluate(tokens)
		arguments.append(value)

	value = function[1](*arguments)
	return value, tokens

if __name__ == '__main__':
	code = get_code()
	tokens = get_tokens(code)
	value, _ = evaluate(tokens)
	print(value)
	print(functions)
