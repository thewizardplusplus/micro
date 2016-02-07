#!/usr/bin/env python

from function import function
from boolean import boolean
from nil import nil_instance
from list import str_to_list, list_to_str
from builtin_functions import builtin_functions
from functions import parent_name, add_assignment, add_assignment_to_parent
from evaluate_list import evaluate_list
from lexer import read_code, remove_comments, tokenize

from re import sub as re_sub
from sys import stdin, stdout
from string import punctuation
from re import DOTALL, escape, IGNORECASE, findall
from copy import copy

if __name__ == '__main__':
	code = read_code()
	code = remove_comments(code)
	print(code)
	tokens = tokenize(code)
	print(tokens)
	value, _ = evaluate_list(tokens, {}, builtin_functions)
	print('')
	print(value)
	print(builtin_functions)
