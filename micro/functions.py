from function import function
from list import list_to_str
from boolean import boolean

parent_name = ':parent'

def search_name(functions, name):
    if not functions:
        return None
    elif name in functions:
        return functions[name]
    else:
        return search_name(get_parent(functions), name)

def add_assignment(functions):
    functions['='] = function(
        lambda name, value: add_value(functions, name, value),
        arity=2
    )

def add_assignment_to_parent(functions):
    functions[':='] = function(
        lambda name, value: add_value_to_parent(functions, name, value),
        arity=2
    )

def is_define(functions, name):
    name = list_to_str(name)
    result = name in functions
    return boolean(result)

def add_is_define(functions):
    functions['is_def'] = function(
        lambda name: is_define(functions, name),
        arity=1
    )

def get_parent(functions):
    if parent_name not in functions:
        functions[parent_name] = {}

    return functions[parent_name]

def add_value(functions, name, value):
    new_name = list_to_str(name)
    new_value = function(lambda: value, arity=0, body=[str(value)])
    functions[new_name] = new_value

    return value

def add_value_to_parent(functions, name, value):
    return add_value(get_parent(functions), name, value)
