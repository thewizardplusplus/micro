ESCAPING_MAP = {'"': r'\"', '\\': r'\\', '\t': r'\t', '\n': r'\n'}

def quote(string):
    escaped_string = ''
    for character in string:
        if character in ESCAPING_MAP:
            escaped_string += ESCAPING_MAP[character]
        else:
            escaped_string += character

    return '"' + escaped_string + '"'
