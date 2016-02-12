from functions import search_name, add_assignment, add_assignment_to_parent
from nil import nil_instance
from lexer import remove_comments, tokenize
import builtin_functions
import parsers
from function import function
from copy import copy

def evaluate_list(tokens, variables):
    add_assignment(variables)
    add_assignment_to_parent(variables)

    result = nil_instance
    while tokens:
        result, tokens = evaluate(tokens, variables)

    return result, tokens

def evaluate_string(str):
    code = remove_comments(str)
    tokens = tokenize(code)
    result, _ = evaluate_list(tokens, builtin_functions.builtin_functions)
    return result

def evaluate(tokens, variables):
    name = tokens[0]
    tokens = tokens[1:]
    result = nil_instance
    if name == 'fn':
        name, result, tokens = parsers.parse_function(tokens, variables)
        if name:
            variables[name] = result
    else:
        value = search_name(variables, name)
        if value is not None:
            result = value
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
        result, tokens = evaluate_function(result, tokens, variables)

    return result, tokens

def evaluate_function(function_instance, tokens, variables):
    arguments, tokens = evaluate_arguments(
        function_instance.arity,
        tokens,
        variables
    )
    if len(arguments) == function_instance.arity:
        result = function_instance.handle(*arguments)
        if isinstance(result, function):
            result, tokens = evaluate_function(
                result,
                tokens,
                variables
            )
    else:
        result = make_closure(function_instance, arguments)

    return result, tokens

def evaluate_arguments(number, tokens, variables):
    arguments = []
    for _ in xrange(number):
        if not tokens or tokens[0] == "'":
            tokens = tokens[1:]
            break

        value, tokens = evaluate(tokens, variables)
        arguments.append(value)

    return arguments, tokens

def make_closure(function_instance, arguments):
    handle = lambda *parameters: closure_body(
        function_instance.handle,
        arguments,
        parameters
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
