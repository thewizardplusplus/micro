from . import error
from . import function_type
from . import string_utilities
from . import utilities
from . import lexer
from . import preparser
from . import ast_node

class Parser:
    def __init__(self):
        self._errors = []

    def parse(self, preast, functions={}):
        self._transform_entity_list(preast, functions)
        return preast

    def get_errors(self):
        return self._errors

    def _transform_entity_list(self, entity, functions):
        entity.children = self._make_calls(entity.children, functions)

    def _make_calls(self, entities, functions):
        calls = []
        while len(entities) > 0:
            call, entities = self._make_call(
                entities[0],
                entities[1:],
                functions,
            )
            if call is None:
                continue

            calls.append(call)

        return calls

    def _make_call(self, first_entity, rest_entities, functions):
        entity_type = self._get_type(first_entity, functions)
        if entity_type is None:
            return None, rest_entities

        parameters = []
        while len(parameters) < entity_type.arity and len(rest_entities) > 0:
            call, rest_entities = self._make_call(
                rest_entities[0],
                rest_entities[1:],
                functions,
            )
            if call is None:
                continue

            parameters.append(call)
        if len(parameters) < entity_type.arity:
            self._errors.append(
                error.Error(
                    'not enough arguments for the call {}'.format(first_entity),
                    first_entity.offset,
                ),
            )

            return None, rest_entities

        if first_entity.name == 'cast':
            self._transform_cast(first_entity, functions)
        if not entity_type.is_callable():
            if first_entity.name == 'function':
                self._transform_function(first_entity, functions)
            elif first_entity.name == 'assignment':
                self._transform_assignment(first_entity, functions)

            return first_entity, rest_entities
        else:
            return self._make_call(
                _make_call_node(first_entity, entity_type, parameters),
                rest_entities,
                functions,
            )

    def _get_type(self, entity, functions):
        entity_type = function_type.make_type([])
        if entity.name == 'IDENTIFIER':
            if entity.value in functions:
                entity_type = functions[entity.value]
            else:
                self._errors.append(
                    error.Error(
                        'unknown function {}'.format(
                            string_utilities.quote(entity.value),
                        ),
                        entity.offset,
                    ),
                )

                entity_type = None
        elif entity.name == 'cast':
            entity_type = function_type.make_type(entity.children[1])
        elif entity.name == 'call':
            entity_type = function_type.make_type(
                entity.children[0].children[1].children[0],
            )

        return entity_type

    def _transform_function(self, entity, functions):
        utilities.extract_and_add_function(entity, functions)

        new_functions = functions.copy()
        for argument in entity.children[0].children[1].children:
            new_functions[argument.children[0].value] = function_type.make_type(
                argument.children[1],
            )

        self._transform_entity_list(entity.children[1], new_functions)

    def _transform_assignment(self, entity, functions):
        new_functions = functions.copy()
        utilities.extract_and_add_assignment(entity, functions)

        self._transform_entity_list(entity.children[1], new_functions)

    def _transform_cast(self, entity, functions):
        self._transform_entity_list(entity.children[0], functions.copy())

def parse_code(code, functions={}, target='ast'):
    specific_lexer = lexer.Lexer()
    if target == 'tokens':
        return specific_lexer.tokenize(code), specific_lexer.get_errors()

    specific_preparser = preparser.Preparser(specific_lexer)
    preast = specific_preparser.preparse(code)
    errors = specific_lexer.get_errors() + specific_preparser.get_errors()
    if target == 'preast':
        return preast, errors

    specific_parser = Parser()
    return specific_parser.parse(preast, functions), \
        errors + specific_parser.get_errors()

def _make_call_node(entity, entity_type, parameters):
    call_node = ast_node.AstNode('call', children=[
        ast_node.AstNode('inner_function', children=[
            ast_node.AstNode('inner_call', children=[entity]),
            ast_node.AstNode('result', children=[
                entity_type.get_result().to_ast(),
            ]),
        ]),
        ast_node.AstNode('parameter_list', children=parameters),
    ])
    call_node.set_offset(entity.offset)

    return call_node
