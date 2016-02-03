#!/usr/bin/env python

from re import sub as re_sub
from sys import stdin
from string import punctuation
from re import DOTALL, escape, IGNORECASE, findall
from operator import add, sub, mul, div
from copy import copy

class function:
	def __init__(self, handle, arguments=None, arity=None, body=[]):
		self.handle = handle
		self.arguments = arguments
		self.body = body

		if not arguments is None:
			self.arity = len(arguments)
		elif not arity is None:
			self.arity = arity

			self.arguments = []
			for i in range(arity):
				argument = '_{:d}'.format(i)
				self.arguments.append(argument)
		else:
			raise Exception('invalid arguments of the function object')

	def __repr__(self):
		body = ' '.join(self.body) if self.body else '[unknown]'
		body = re_sub(r"\s?(\(|\))\s?", r'\1', body)
		body = re_sub(r"\s(;|')", r'\1', body)
		body = re_sub("';", ';', body)
		body = re_sub(r'^fn\(\)(.*);$', r'\1', body)

		arguments = ' '.join(self.arguments)
		return 'fn({:s}){:s};'.format(arguments, body)

functions = { \
	'+': function(add, arity=2), \
	'-': function(sub, arity=2), \
	'*': function(mul, arity=2), \
	'/': function(div, arity=2) \
}

def head(list):
	return list[0]

def tail(list):
	return list[1:]

def apply(function, arguments):
	return function(*arguments)

def get_code():
	return stdin.read()

def remove_comments(code):
	code = re_sub(r'\bnb:.*\bnb;', '', code, flags=DOTALL)
	code = re_sub(r'\bnb\b.*\n', '', code)
	return code

def get_tokens(code):
	allowed_punctuation = escape(punctuation.translate(None, "();'"))
	grammar = r"[a-z_]+|\d+|\(|\)|;|'|[{:s}]+".format(allowed_punctuation)
	tokens = findall(grammar, code, IGNORECASE)
	return filter(lambda token: token.strip(), tokens)

def parse_function_name(tokens):
	name = ''
	if head(tokens) != '(':
		name = head(tokens)
		if name in functions:
			raise Exception( \
				'found a duplicate of the "{:s}" function'.format(name) \
			)

		tokens = tail(tokens)

	# cut the open parenthesis
	tokens = tail(tokens)

	return name, tokens

def parse_function_arguments(tokens):
	arguments = []
	while head(tokens) != ')':
		arguments.append(head(tokens))
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

def custom_handle(tokens, variables, names, values):
	new_variables = dict(zip(names, values))
	new_variables = dict(variables.items() + new_variables.items())
	value, _ = evaluate(tokens, new_variables)
	return value

def parse_function(tokens, variables):
	name, tokens = parse_function_name(tokens)
	arguments, tokens = parse_function_arguments(tokens)
	body, tokens = parse_function_body(tokens)
	handle = lambda *parameters: custom_handle( \
		body, \
		variables, \
		arguments, \
		parameters \
	)
	return name, function(handle, arguments=arguments, body=body), tokens

def evaluate_arguments(tokens, variables, number):
	arguments = []
	for _ in xrange(number):
		if not tokens or head(tokens) == "'":
			tokens = tail(tokens)
			break

		value, tokens = evaluate(tokens, variables)
		arguments.append(value)

	return arguments, tokens

def closure(handle, primary_arguments, secondary_arguments):
	return apply(handle, primary_arguments + list(secondary_arguments))

def evaluate_function(function_object, tokens, variables):
	arguments, tokens = evaluate_arguments( \
		tokens, \
		variables, \
		function_object.arity \
	)
	if len(arguments) < function_object.arity:
		handle = lambda *parameters: closure( \
			function_object.handle, \
			arguments, \
			parameters \
		)

		new_arguments = function_object.arguments[len(arguments):]
		rest_arguments = function_object.arguments[:len(arguments)]

		function_object_copy = copy(function_object)
		function_object_copy.arguments = rest_arguments
		body = [str(function_object_copy)] + map(str, arguments)

		return function(handle, arguments=new_arguments, body=body), tokens

	result = apply(function_object.handle, arguments)
	if isinstance(result, function):
		return evaluate_function(result, tokens, variables)

	return result, tokens

def evaluate(tokens, variables):
	name = head(tokens)
	tokens = tail(tokens)
	result = None
	if name == 'fn':
		name, result, tokens = parse_function(tokens, variables)
		if name:
			functions[name] = result
	elif name in variables:
		result = variables[name]
	elif name in functions:
		result = functions[name]
	else:
		result = int(name)

	if isinstance(result, function):
		result, tokens = evaluate_function(result, tokens, variables)

	return result, tokens

def evaluate_list(tokens):
	result = None
	while tokens:
		result, tokens = evaluate(tokens, {})

	return result

if __name__ == '__main__':
	code = get_code()
	code = remove_comments(code)
	tokens = get_tokens(code)
	value = evaluate_list(tokens)
	print(value)
	print(functions)
