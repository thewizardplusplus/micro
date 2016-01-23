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

def head(list):
	return list[0]

def tail(list):
	return list[1:]

def apply(function, arguments):
	return function(*arguments)

def get_code():
	return argv[1]

def get_tokens(code):
	return code.split(' ')

def generate_name():
	return str(uuid4())

def parse_function_name(tokens):
	name = ''
	if head(tokens) != '(':
		name = head(tokens)
		if name in functions:
			raise Exception( \
				'found a duplicate of the "{:s}" function'.format(name) \
			)

		tokens = tail(tokens)
	else:
		name = generate_name()

	# cut the open parenthesis
	tokens = tail(tokens)

	return name, tokens

def parse_function_arguments(tokens):
	arguments = 0
	while head(tokens) != ')':
		arguments += 1
		tokens = tail(tokens)

	# cut the close parenthesis
	tokens = tail(tokens)

	return arguments, tokens

def parse_function_body(tokens):
	level = 1
	body = []
	while level > 0:
		if head(tokens) == 'fn':
			level += 1
		if head(tokens) == ';':
			level -= 1

		# except the final semicolon
		if level > 0:
			body.append(head(tokens))
		tokens = tail(tokens)

	return body, tokens

def parse_function(tokens):
	name, tokens = parse_function_name(tokens)
	arguments, tokens = parse_function_arguments(tokens)
	body, tokens = parse_function_body(tokens)
	return name, (arguments, body), tokens

def evaluate_arguments(tokens, number):
	arguments = []
	for _ in xrange(number):
		value, tokens = evaluate(tokens)
		arguments.append(value)

	return arguments, tokens

def evaluate(tokens):
	name = head(tokens)
	tokens = tail(tokens)
	if name == 'fn':
		name, function, tokens = parse_function(tokens)
		functions[name] = function

		return 0, tokens
	if name not in functions:
		return int(name), tokens

	arguments, tokens = evaluate_arguments(tokens, functions[name][0])
	value = apply(functions[name][1], arguments)

	return value, tokens

if __name__ == '__main__':
	code = get_code()
	tokens = get_tokens(code)
	value, _ = evaluate(tokens)
	print(value)
	print(functions)
