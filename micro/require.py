from list import list_to_str, str_to_list
from os.path import join, abspath
from nil import nil_instance
import evaluate_list

require_cache = {}

def require(base_path, path):
    result = nil_instance
    path = custom_join_path(base_path, path)
    with open(path, 'r') as file:
        code = file.read()
        result = evaluate_list.evaluate_string(code)

    require_cache[path] = result
    return result

def require_once(base_path, path):
    result = nil_instance
    path = custom_join_path(base_path, path)
    if path not in require_cache:
        path = str_to_list(path)
        result = require(path)
    else:
        result = require_cache[path]

    return result

def custom_join_path(base_path, path):
    path = list_to_str(path)
    path = join(base_path, path)
    return abspath(path)
