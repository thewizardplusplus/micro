import os

import function_type
import string_utilities

def extract_and_add_function(entity, functions):
    entity_type = function_type.FunctionType(
        len(entity.children[0].children[1].children),
        function_type.make_type(entity.children[0].children[2].children[0]),
    )
    _add_to_functions(
        functions,
        entity.children[0].children[0].value,
        entity_type,
    )

    return entity_type

def extract_and_add_assignment(entity, functions):
    entity_type = function_type.make_type(entity.children[0].children[1])
    _add_to_functions(
        functions,
        entity.children[0].children[0].value,
        entity_type,
    )

    return entity_type

def get_environment_variable(name):
    value = os.getenv(string_utilities.make_string_from_list(name))
    if value is None:
        return None

    return string_utilities.make_list_from_string(value)

def _add_to_functions(functions, entity_name, entity_type):
    if entity_name != '':
        functions[entity_name] = entity_type
