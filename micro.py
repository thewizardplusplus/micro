#!/usr/bin/env python

from lexer import read_code, remove_comments, tokenize
from builtin_functions import builtin_functions
from evaluate_list import evaluate_list

if __name__ == '__main__':
	code = read_code()
	code = remove_comments(code)

	tokens = tokenize(code)
	evaluate_list(tokens, {}, builtin_functions)
