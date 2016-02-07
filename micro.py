#!/usr/bin/env python

from function import function
from boolean import boolean
from nil import nil_instance
from list import str_to_list, list_to_str
from builtin_functions import builtin_functions
from functions import parent_name, add_assignment, add_assignment_to_parent
from evaluate_list import evaluate_list

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
