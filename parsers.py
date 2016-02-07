from function import function
from list import str_to_list
from nil import nil_instance
from copy import copy
from functions import parent_name
import evaluate_list

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
	function_instance = function(handle, arguments=arguments, body=body)
	return name, function_instance, tokens

def parse_string(str):
	if len(str) == 1 or str[-1] != '"':
		raise Exception('invalid string token {:s}'.format(repr(str)))

	str = str.strip('"').decode('string_escape')
	return str_to_list(str)

def parse_character(str):
	if len(str) == 1 or str[-1] != '`':
		raise Exception('invalid character token {:s}'.format(repr(str)))

	str = str.strip('`').decode('string_escape')
	if len(str) != 1:
		raise Exception( \
			'invalid length of character token {:s}'.format(repr(str)) \
		)

	return ord(str)

def parse_number(str):
	result = nil_instance
	try:
		result = int(str)
	except ValueError:
		result = float(str)

	return result

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

def custom_handle(tokens, variables, names, values):
	new_variables = dict(zip(names, values))
	new_variables = dict(variables.items() + new_variables.items())
	new_variables[parent_name] = variables

	value, _ = evaluate_list.evaluate_list(tokens, new_variables)
	return value
