#!/usr/bin/env python

from sys import argv

def get_code():
	return argv[1]

def get_tokens(code):
	return code.split(' ')

if __name__ == '__main__':
	code = get_code()
	tokens = get_tokens(code)
	print(tokens)
