import os.path

from . import function_type

MICRO_VERSION = '2.3'
HEXADECIMAL_NUMBER = '[A-Fa-f0-9]'

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

def make_arguments_processor(argument_handler):
    return lambda function: \
        lambda *arguments: \
            function(*list(map(argument_handler, arguments)))

def get_base_path(filename):
    base_path = None
    if filename is not None and filename != '-':
        base_path = os.path.dirname(filename)

    return base_path

def _add_to_functions(functions, entity_name, entity_type):
    if entity_name != '':
        functions[entity_name] = entity_type
