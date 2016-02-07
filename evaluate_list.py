from functions import parent_name, add_assignment, add_assignment_to_parent
from nil import nil_instance
import parse_function
from list import str_to_list
from function import function

def evaluate_list(tokens, variables, functions):
	add_assignment(functions)
	add_assignment_to_parent(functions)

	result = nil_instance
	while tokens:
		result, tokens = evaluate(tokens, variables, functions)

	return result, tokens

def evaluate(tokens, variables, functions):
	name = tokens[0]
	tokens = tokens[1:]
	result = nil_instance
	if name == 'fn':
		name, result, tokens = parse_function.parse_function( \
			tokens, \
			variables, \
			functions \
		)
		if name:
			functions[name] = result
	elif name in variables:
		result = variables[name]
	elif name in functions:
		result = functions[name]
	elif parent_name in functions and name in functions[parent_name]:
		result = functions[parent_name][name]
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

def evaluate_function(function_instance, tokens, variables, functions):
	arguments, tokens = evaluate_arguments( \
		function_instance.arity, \
		tokens, \
		variables, \
		functions \
	)
	if len(arguments) < function_instance.arity:
		handle = lambda *parameters: closure_body( \
			function_instance.handle, \
			arguments, \
			parameters \
		)

		new_arguments = function_instance.arguments[len(arguments):]
		rest_arguments = function_instance.arguments[:len(arguments)]

		function_instance_copy = copy(function_instance)
		function_instance_copy.arguments = rest_arguments
		body = [str(function_instance_copy)] + map(str, arguments)

		return function(handle, arguments=new_arguments, body=body), tokens

	result = function_instance.handle(*arguments)
	if isinstance(result, function):
		return evaluate_function(result, tokens, variables, functions)

	return result, tokens

def evaluate_arguments(number, tokens, variables, functions):
	arguments = []
	for _ in xrange(number):
		if not tokens or tokens[0] == "'":
			tokens = tokens[1:]
			break

		value, tokens = evaluate(tokens, variables, functions)
		arguments.append(value)

	return arguments, tokens

def closure_body(handle, primary_arguments, secondary_arguments):
	arguments = primary_arguments + list(secondary_arguments)
	return handle(*arguments)
