#!/usr/bin/env python

from function import function
from boolean import boolean
from nil import nil_instance
from list import str_to_list, list_to_str
from builtin_functions import builtin_functions

from re import sub as re_sub
from sys import stdin, stdout
from string import punctuation
from re import DOTALL, escape, IGNORECASE, findall
from copy import copy

def get_code():
	return stdin.read()

def remove_comments(code):
	code = re_sub(r'\bnb:.*\bnb;', '', code, flags=DOTALL)
	code = re_sub(r'\bnb\b.*\n', '', code)
	return code

def get_tokens(code):
	allowed_punctuation = escape(punctuation.translate(None, '_.();\'`"'))
	grammar = '[a-z_]+' \
		+ r'|(?:\d+(?:\.\d+)?)' \
		+ r'|\(' \
		+ r'|\)' \
		+ '|;' \
		+ "|'" \
		+ r'|(?:`(?:\\.|[^`])*`?)' \
		+ r'|(?:"(?:\\.|[^"])*"?)' \
		+ '|[{:s}]+'
	grammar = grammar.format(allowed_punctuation)
	tokens = findall(grammar, code, IGNORECASE)
	return filter(lambda token: token.strip(), tokens)

def parse_function_name(tokens):
	name = ''
	if tokens[0] != '(':
		name = tokens[0]
		tokens = tokens[1:]

	# cut the open parenthesis
	tokens = tokens[1:]

	return name, tokens

def parse_function_arguments(tokens):
	arguments = []
	while tokens[0] != ')':
		arguments.append(tokens[0])
		tokens = tokens[1:]

	# cut the close parenthesis
	tokens = tokens[1:]

	return arguments, tokens

def parse_function_body(tokens):
	level = 1
	body = []
	while level > 0:
		if tokens[0] == 'fn':
			level += 1
		if tokens[0] == ';':
			level -= 1

		# except the final semicolon
		if level > 0:
			body.append(tokens[0])
		tokens = tokens[1:]

	return body, tokens

def custom_handle(tokens, variables, functions, names, values):
	new_variables = dict(zip(names, values))
	new_variables = dict(variables.items() + new_variables.items())

	new_functions = copy(functions)
	new_functions[':parent'] = functions

	value, _ = evaluate_list(tokens, new_variables, new_functions)
	return value

def parse_function(tokens, variables, functions):
	name, tokens = parse_function_name(tokens)
	arguments, tokens = parse_function_arguments(tokens)
	body, tokens = parse_function_body(tokens)
	handle = lambda *parameters: custom_handle( \
		body, \
		variables, \
		functions, \
		arguments, \
		parameters \
	)
	return name, function(handle, arguments=arguments, body=body), tokens

def evaluate_arguments(number, tokens, variables, functions):
	arguments = []
	for _ in xrange(number):
		if not tokens or tokens[0] == "'":
			tokens = tokens[1:]
			break

		value, tokens = evaluate(tokens, variables, functions)
		arguments.append(value)

	return arguments, tokens

def closure(handle, primary_arguments, secondary_arguments):
	arguments = primary_arguments + list(secondary_arguments)
	return handle(*arguments)

def evaluate_function(function_object, tokens, variables, functions):
	arguments, tokens = evaluate_arguments( \
		function_object.arity, \
		tokens, \
		variables, \
		functions \
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

	result = function_object.handle(*arguments)
	if isinstance(result, function):
		return evaluate_function(result, tokens, variables, functions)

	return result, tokens

def evaluate(tokens, variables, functions):
	name = tokens[0]
	tokens = tokens[1:]
	result = None
	if name == 'fn':
		name, result, tokens = parse_function(tokens, variables, functions)
		if name:
			functions[name] = result
	elif name in variables:
		result = variables[name]
	elif name in functions:
		result = functions[name]
	elif ':parent' in functions and name in functions[':parent']:
		result = functions[':parent'][name]
	elif name[0] == '"':
		if len(name) == 1 or name[-1] != '"':
			raise Exception('invalid string token {:s}'.format(repr(name)))

		name = name.strip('"').decode('string_escape')
		result = str_to_list(name)
	elif name[0] == '`':
		if len(name) == 1 or name[-1] != '`':
			raise Exception('invalid character token {:s}'.format(repr(name)))

		name = name.strip('`').decode('string_escape')
		if len(name) != 1:
			raise Exception( \
				'invalid length of character token {:s}'.format(repr(name)) \
			)

		result = ord(name)
	else:
		try:
			result = int(name)
		except ValueError:
			try:
				result = float(name)
			except ValueError:
				raise Exception('unknown function {:s}'.format(repr(name)))

	if isinstance(result, function):
		result, tokens = evaluate_function(result, tokens, variables, functions)

	return result, tokens

def add_value(functions, name, value):
	new_name = list_to_str(name)
	new_value = function(lambda: value, arity=0)
	functions[new_name] = new_value

	return value

def get_parent(functions):
	if not ':parent' in functions:
		functions[':parent'] = {}

	return functions[':parent']

def evaluate_list(tokens, variables, functions):
	functions['='] = function( \
		lambda name, value: add_value(functions, name, value),
		arity=2 \
	)
	functions[':='] = function( \
		lambda name, value: add_value(get_parent(functions), name, value),
		arity=2 \
	)

	result = nil_instance
	while tokens:
		result, tokens = evaluate(tokens, variables, functions)

	return result, tokens

if __name__ == '__main__':
	code = get_code()
	code = remove_comments(code)
	print(code)
	tokens = get_tokens(code)
	print(tokens)
	value, _ = evaluate_list(tokens, {}, builtin_functions)
	print('')
	print(value)
	print(builtin_functions)
