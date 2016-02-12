from list import list_to_str, str_to_list
from os.path import abspath
from nil import nil_instance
import evaluate_list

require_cache = {}

def require(path):
    result = nil_instance
    path = list_to_str(path)
    with open(path, 'r') as file:
        code = file.read()
        result = evaluate_list.evaluate_string(code)

        path = abspath(path)
        if path not in require_cache:
            require_cache[path] = result

    return result

def require_once(path):
    path = list_to_str(path)
    path = abspath(path)

    result = nil_instance
    if path not in require_cache:
        path = str_to_list(path)
        result = require(path)
    else:
        result = require_cache[path]

    return result
