import ast_node
import utilities
import error

class Parser:
    _errors = []

    def __init__(self, functions={}):
        self._functions = functions

    def parse(self, preast):
        preast.children = self._make_calls(preast.children, self._functions)
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
        if entity_type.arity is None:
            return None, rest_entities

        arguments = []
        arity = entity_type.arity
        while arity > 0 and len(rest_entities) > 0:
            call, rest_entities = self._make_call(rest_entities[0], rest_entities[1:], functions)
            if call is None:
                continue

            arguments.append(call)
            arity -= 1
        if arity > 0:
            self._errors.append(error.Error('{}'.format(utilities.quote('dummy')), 0))
            return None, rest_entities

        if len(arguments) == 0:
            if first_entity.name == 'function':
                result_type = function_type.make_type(first_entity.children[0].children[2].children[0])
                first_entity.children[0].children[2].children[0] = result_type.to_ast()

                first_entity.children[1].children = self._make_calls(first_entity.children[1].children, functions)

            return first_entity, rest_entities
        else:
            call = self._make_call_node(first_entity, entity_type, arguments)
            return self._make_call(call, rest_entities, functions)

    def _get_type(self, entity, functions):
        entity_type = function_type.make_type([])
        if entity.name == 'IDENTIFIER':
            if entity.value in self._functions:
                entity_type = functions[entity.value]
            else:
                self._errors.append(error.Error('unknown function {}'.format(utilities.quote(entity.value)), entity.offset))
                entity_type = None
        elif entity.name == 'call':
            entity_type = function_type.make_type(entity.children[0].children[1].children[0])

        return entity_type

    def _make_call_node(self, entity, entity_type, arguments):
        inner_call_node = ast_node.AstNode('inner_call', children=[entity])
        type_node = entity_type.get_result().to_ast()
        result_node = ast_node.AstNode('result', children=[type_node])
        inner_function_node = ast_node.AstNode('inner_function', children=[inner_call_node, result_node])
        arguments_node = ast_node.AstNode('argument_list', children=arguments)
        return ast_node.AstNode('call', children=[inner_function_node, arguments_node])

if __name__ == '__main__':
    import function_type
    import read_code
    import lexer
    import preparser

    FUNCTIONS = {
        '@': function_type.make_type([]),
        '~': function_type.make_type([1]),
        '+': function_type.make_type([2]),
        'rand': function_type.make_type([1, 1, 1])
    }

    code = read_code.read_code()
    specific_lexer = lexer.Lexer()
    specific_preparser = preparser.Preparser(specific_lexer)
    preast = specific_preparser.preparse(code)
    parser = Parser(FUNCTIONS)
    ast = parser.parse(preast)
    print(ast)

    for some_error in specific_lexer.get_errors() + specific_preparser.get_errors() + parser.get_errors():
        some_error.detect_position(code)
        print(some_error)
