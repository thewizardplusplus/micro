from function import function
from copy import copy
from functions import parent_name
import evaluate_list

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
	function_instance = function(handle, arguments=arguments, body=body)
	return name, function_instance, tokens

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
	new_functions[parent_name] = functions

	value, _ = evaluate_list.evaluate_list(tokens, new_variables, new_functions)
	return value
