from sys import stdin
from re import DOTALL, sub, escape, IGNORECASE, findall
from string import punctuation

def read_code():
	return stdin.read()

def remove_comments(code):
	code = sub(r'\bnb:.*\bnb;', '', code, flags=DOTALL)
	code = sub(r'\bnb\b.*\n', '', code)
	return code

def tokenize(code):
	allowed_punctuation = punctuation.translate(None, '_.();\'`"')
	allowed_punctuation = escape(allowed_punctuation)

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
