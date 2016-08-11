import error
import function_type
import string_utilities
import utilities
import ast_node

class Parser:
    _errors = []

    def parse(self, preast, functions={}):
        preast.children = self._make_calls(preast.children, functions)
        return preast

    def get_errors(self):
        return self._errors

    def _make_calls(self, entities, functions):
        calls = []
        while len(entities) > 0:
            call, entities = self._make_call(entities[0], entities[1:], functions)
            if call is None:
                continue

            calls.append(call)

        return calls

    def _make_call(self, first_entity, rest_entities, functions):
        entity_type = self._get_type(first_entity, functions)
        if entity_type is None:
            return None, rest_entities

        parameters = []
        arity = entity_type.arity
        while arity > 0 and len(rest_entities) > 0:
            call, rest_entities = self._make_call(rest_entities[0], rest_entities[1:], functions)
            if call is None:
                continue

            parameters.append(call)
            arity -= 1
        if arity > 0:
            self._errors.append(error.Error('not enough arguments for the call {}'.format(first_entity), first_entity.offset))
            return None, rest_entities

        if not entity_type.is_callable():
            if first_entity.name == 'function':
                self._transform_function(first_entity, functions)

            return first_entity, rest_entities
        else:
            call = _make_call_node(first_entity, entity_type, parameters)
            return self._make_call(call, rest_entities, functions)

    def _get_type(self, entity, functions):
        entity_type = function_type.make_type([])
        if entity.name == 'IDENTIFIER':
            if entity.value in functions:
                entity_type = functions[entity.value]
            else:
                self._errors.append(error.Error('unknown function {}'.format(string_utilities.quote(entity.value)), entity.offset))
                entity_type = None
        elif entity.name == 'call':
            entity_type = function_type.make_type(entity.children[0].children[1].children[0])

        return entity_type

    def _transform_function(self, entity, functions):
        name, entity_type = utilities.extract_function(entity)
        if name != '':
            functions[name] = entity_type

        new_functions = functions.copy()
        for argument in entity.children[0].children[1].children:
            new_functions[argument.children[0].value] = function_type.make_type(argument.children[1])
        entity.children[1].children = self._make_calls(entity.children[1].children, new_functions)

def _make_call_node(entity, entity_type, parameters):
    inner_call_node = ast_node.AstNode('inner_call', children=[entity])
    type_node = entity_type.get_result().to_ast()
    result_node = ast_node.AstNode('result', children=[type_node])
    inner_function_node = ast_node.AstNode('inner_function', children=[inner_call_node, result_node])
    parameters_node = ast_node.AstNode('parameter_list', children=parameters)
    call_node = ast_node.AstNode('call', children=[inner_function_node, parameters_node])
    call_node.set_offset(entity.offset)

    return call_node

if __name__ == '__main__':
    import read_code
    import lexer
    import preparser

    FUNCTIONS = {
        '@': function_type.make_type([]),
        '~': function_type.make_type([1]),
        '+': function_type.make_type([2]),
        'rand': function_type.make_type([1, 1, 1]),
        'range': function_type.make_type([0, 2])
    }

    code = read_code.read_code()
    specific_lexer = lexer.Lexer()
    specific_preparser = preparser.Preparser(specific_lexer)
    preast = specific_preparser.preparse(code)
    parser = Parser()
    ast = parser.parse(preast, FUNCTIONS)
    print(ast)

    for some_error in specific_lexer.get_errors() + specific_preparser.get_errors() + parser.get_errors():
        some_error.detect_position(code)
        print(some_error)
