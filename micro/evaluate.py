import function_type
import string_utilities
import utilities
import trampoline

def evaluate(ast, functions={}):
    result = None
    for entity in ast.children:
        result = _evaluate_entity(entity, functions)

    return result

def _evaluate_entity(entity, functions):
    if entity.name == 'INTEGRAL_NUMBER' or entity.name == 'REAL_NUMBER':
        return float(entity.value)
    elif entity.name == 'CHARACTER':
        return float(ord(string_utilities.unquote(entity.value)))
    elif entity.name == 'STRING':
        return string_utilities.make_list_from_string(
            string_utilities.unquote(entity.value),
        )
    elif entity.name == 'IDENTIFIER':
        return trampoline.closure_trampoline(functions[entity.value])
    elif entity.name == 'function':
        return _evaluate_function(entity, functions)
    elif entity.name == 'assignment':
        return _evaluate_assignment(entity, functions)
    elif entity.name == 'cast':
        return _evaluate_cast(entity, functions)
    elif entity.name == 'call':
        return _evaluate_call(entity, functions)
    else:
        raise Exception('the unexpected entity {}'.format(entity))

def _evaluate_function(entity, functions):
    entity_type = utilities.extract_and_add_function(entity, functions)
    entity_type.handler = _make_function_handler(entity, functions.copy())

    return entity_type

def _make_function_handler(function_node, functions):
    def handler(*args):
        for i, argument in enumerate(
            function_node.children[0].children[1].children,
        ):
            entity_type = function_type.make_type(argument.children[1])
            entity_type.handler = _make_value_wrapper(args[i], entity_type)

            functions[argument.children[0].value] = entity_type

        return evaluate(function_node.children[1], functions)

    return handler

def _make_value_wrapper(value, value_type):
    return value if value_type.arity > 0 else lambda: value

def _evaluate_assignment(entity, functions):
    entity_type = utilities.extract_and_add_assignment(entity, functions)
    entity_type.handler = _make_value_wrapper(
        evaluate(entity.children[1], functions.copy()),
        entity_type,
    )

    return entity_type

def _evaluate_cast(entity, functions):
    return evaluate(entity.children[0], functions.copy())

def _evaluate_call(call, functions):
    inner_function = _evaluate_entity(
        call.children[0].children[0].children[0],
        functions,
    )
    parameters = [
        _evaluate_entity(parameter, functions)
        for parameter in call.children[1].children
    ]
    return trampoline.closure_trampoline(inner_function(*parameters))
