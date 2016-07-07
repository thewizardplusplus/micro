ESCAPING_MAP = {'"': r'\"', '\\': r'\\', '\t': r'\t', '\n': r'\n'}

def quote(string):
    escaped_string = ''
    for character in string:
        if character in ESCAPING_MAP:
            escaped_string += ESCAPING_MAP[character]
        else:
            escaped_string += character

    return '"' + escaped_string + '"'

def find_column(code, offset):
    last_line_break = code.rfind('\n', 0, offset)
    if last_line_break != -1:
        return offset - last_line_break
    else:
        return offset + 1
