#!/usr/bin/env python

from sys import argv

def get_code():
	return argv[1]

if __name__ == '__main__':
	code = get_code()
	print(code)
