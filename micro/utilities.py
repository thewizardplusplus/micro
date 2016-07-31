import function_type

ESCAPING_MAP = {'"': r'\"', '\\': r'\\', '\t': r'\t', '\n': r'\n'}

def quote(string):
    escaped_string = ''
    for character in string:
        if character in ESCAPING_MAP:
            escaped_string += ESCAPING_MAP[character]
        else:
            escaped_string += character

    return '"' + escaped_string + '"'

def extract_function(function_node):
    name = function_node.children[0].children[0].value
    arity = len(function_node.children[0].children[1].children)
    result_type = function_type.make_type(function_node.children[0].children[2].children[0])
    return name, function_type.FunctionType(arity, result_type)
