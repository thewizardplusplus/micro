import re
import function_type

STRING_CHARACTER_PATTERN = r'\\["\\tn]|(?!\\)[^"]'

_ESCAPING_MAP = {'"': r'\"', '\\': r'\\', '\t': r'\t', '\n': r'\n'}
_UNESCAPING_MAP = {value: key for key, value in _ESCAPING_MAP.items()}
_STRING_CHARACTER_COMPILED_PATTERN = re.compile(STRING_CHARACTER_PATTERN)

def quote(string):
    return '"' + ''.join([_ESCAPING_MAP.get(character, character) for character in string]) + '"'

def unquote(string):
    return _STRING_CHARACTER_COMPILED_PATTERN.sub(lambda matches: _UNESCAPING_MAP.get(matches.group(), matches.group()), string[1:-1])

def extract_function(function_node):
    name = function_node.children[0].children[0].value
    arity = len(function_node.children[0].children[1].children)
    result_type = function_type.make_type(function_node.children[0].children[2].children[0])
    return name, function_type.FunctionType(arity, result_type)
