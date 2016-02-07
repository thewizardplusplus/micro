#!/usr/bin/env python

from function import function
from boolean import boolean
from nil import nil_instance

from re import sub as re_sub
from sys import stdin, stdout
from string import punctuation
from re import DOTALL, escape, IGNORECASE, findall
from numbers import Number
from math import floor, ceil, trunc
from operator import sub, div
from copy import copy

def add(a, b):
	if not isinstance(a, Number) or not isinstance(b, Number):
		raise TypeError( \
			"unsupported operand type(s) for +: '{:s}' and '{:s}'".format( \
				type(a).__name__, \
				type(b).__name__, \
			) \
		)

	return a + b

def mul(a, b):
	if not isinstance(a, Number) or not isinstance(b, Number):
		raise TypeError( \
			"unsupported operand type(s) for *: '{:s}' and '{:s}'".format( \
				type(a).__name__, \
				type(b).__name__, \
			) \
		)

	return a * b

def modulo(a, b):
	if \
		not isinstance(a, Number) \
		or not float(a).is_integer() \
		or not isinstance(b, Number) \
		or not float(b).is_integer() \
	:
		raise TypeError( \
			"unsupported operand type(s) for %: '{:s}' and '{:s}'".format( \
				type(a).__name__, \
				type(b).__name__, \
			) \
		)

	return a % b

def list_to_str(list):
	return ''.join(map(chr, list))

def str_to_list(str):
	return map(ord, str)

def print_function(str):
	if not isinstance(str, list):
		raise TypeError( \
			"unsupported operand type(s) for print: '{:s}'".format( \
				type(str).__name__, \
			) \
		)

	new_str = list_to_str(str)
	stdout.write(new_str)

	return str

def to_string(value):
	return str_to_list(str(value))

def to_number(value):
	if not isinstance(value, list):
		raise TypeError( \
			"unsupported operand type(s) for to_num: '{:s}'".format( \
				type(value).__name__, \
			) \
		)

	new_value = list_to_str(value)
	return float(new_value)

def while_function(condition, body):
	if not isinstance(condition, function) or not isinstance(body, function):
		raise TypeError( \
			"unsupported operand type(s) for while: '{:s}' and '{:s}'".format( \
				type(condition).__name__, \
				type(body).__name__, \
			) \
		)

	result = nil_instance
	while condition.handle(nil_instance):
		result = body.handle(nil_instance)

	return result

functions = { \
	'nil': function(lambda: nil_instance, arity=0), \
	'floor': function(floor, arity=1), \
	'ceil': function(ceil, arity=1), \
	'trunc': function(trunc, arity=1), \
	'+': function(add, arity=2), \
	'-': function(sub, arity=2), \
	'*': function(mul, arity=2), \
	'/': function(div, arity=2), \
	'%': function(modulo, arity=2), \
	'==': function(lambda a, b: boolean(a == b), arity=2), \
	'!=': function(lambda a, b: boolean(a != b), arity=2), \
	'<': function(lambda a, b: boolean(float(a) < float(b)), arity=2), \
	'<=': function(lambda a, b: boolean(float(a) <= float(b)), arity=2), \
	'>': function(lambda a, b: boolean(float(a) > float(b)), arity=2), \
	'>=': function(lambda a, b: boolean(float(a) >= float(b)), arity=2), \
	'true': function(lambda: boolean(True), arity=0), \
	'false': function(lambda: boolean(False), arity=0), \
	'&&': function(lambda a, b: a and b, arity=2), \
	'||': function(lambda a, b: a or b, arity=2), \
	'!': function(lambda a: boolean(not a), arity=1), \
	'if': function(lambda condition, a, b: a if condition else b, arity=3), \
	'$': function(lambda: [], arity=0), \
	':': function(lambda value, list: [value] + list, arity=2), \
	'head': function(lambda list: list[0], arity=1), \
	'tail': function(lambda list: list[1:], arity=1), \
	'print': function(print_function, arity=1), \
	'to_str': function(to_string, arity=1), \
	'to_num': function(to_number, arity=1), \
	'while': function(while_function, arity=2) \
}

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
	value, _ = evaluate_list(tokens, {}, functions)
	print('')
	print(value)
	print(functions)
