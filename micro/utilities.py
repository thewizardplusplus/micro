import re
import function_type

ESCAPING_MAP = {'"': r'\"', '\\': r'\\', '\t': r'\t', '\n': r'\n'}
UNESCAPING_MAP = {value: key for key, value in ESCAPING_MAP.items()}
UNESCAPING_PATTERN = re.compile(r'\\["\\tn]|(?!\\)[^"\n]')

def quote(string):
    return '"' + ''.join([ESCAPING_MAP.get(character, character) for character in string]) + '"'

def unquote(string):
    return UNESCAPING_PATTERN.sub(lambda matches: UNESCAPING_MAP.get(matches.group(), matches.group()), string[1:-1])

def extract_function(function_node):
    name = function_node.children[0].children[0].value
    arity = len(function_node.children[0].children[1].children)
    result_type = function_type.make_type(function_node.children[0].children[2].children[0])
    return name, function_type.FunctionType(arity, result_type)
