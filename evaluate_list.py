from functions import get_parent, add_assignment, add_assignment_to_parent
from nil import nil_instance
import parsers
from function import function
from copy import copy

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
		name, result, tokens = parsers.parse_function( \
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
	elif name in get_parent(functions):
		result = get_parent(functions)[name]
	elif name[0] == '"':
		result = parsers.parse_string(name)
	elif name[0] == '`':
		result = parsers.parse_character(name)
	else:
		try:
			result = parsers.parse_number(name)
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
	if len(arguments) == function_instance.arity:
		result = function_instance.handle(*arguments)
		if isinstance(result, function):
			result, tokens = evaluate_function( \
				result, \
				tokens, \
				variables, \
				functions \
			)
	else:
		result = make_closure(function_instance, arguments)

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

def make_closure(function_instance, arguments):
	handle = lambda *parameters: closure_body( \
		function_instance.handle, \
		arguments, \
		parameters \
	)
	new_arguments = function_instance.arguments[len(arguments):]
	body = closure_body_representation(function_instance, arguments)
	return function(handle, arguments=new_arguments, body=body)

def closure_body(handle, primary_arguments, secondary_arguments):
	arguments = primary_arguments + list(secondary_arguments)
	return handle(*arguments)

def closure_body_representation(function_instance, arguments):
	function_instance_copy = copy(function_instance)

	rest_arguments = function_instance.arguments[:len(arguments)]
	function_instance_copy.arguments = rest_arguments

	return [str(function_instance_copy)] + map(str, arguments)
