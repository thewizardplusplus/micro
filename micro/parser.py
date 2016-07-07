import ast_node
import utilities
import error

class Parser:
    _errors = []

    def __init__(self, functions={}):
        self._functions = functions

    def parse(self, preast):
        preast.children = self._make_call_list(preast.children)
        return preast

    def get_errors(self):
        return self._errors

    def _make_call_list(self, entities):
        calls = []
        while len(entities) > 0:
            call, entities = self._make_call(entities)
            if call is None:
                continue
            if call.name == 'function':
                call.children[1].children = self._make_call_list(call.children[1].children)
            if call.name == 'call' and call.children[1].children[-1].name == 'closure_mark':
                call = self._make_closure_node(call)

            calls.append(call)

        return calls

    def _make_call(self, entities):
        entity, entities = entities[0], entities[1:]
        arity = self._get_arity(entity)
        if arity is None:
            return None, entities

        arguments = []
        while arity > 0 and len(entities) > 0:
            call, entities = self._make_call(entities)
            if call is None:
                continue
            if call.name == 'closure_mark':
                break

            arguments.append(call)
            arity -= 1

        if arity > 0:
            arguments.append(ast_node.AstNode('closure_mark'))

        return self._make_call_node(entity, arguments), entities

    def _get_arity(self, entity):
        arity = 0
        if entity.name == 'IDENTIFIER':
            if entity.value in self._functions:
                arity = self._functions[entity.value]
            else:
                self._errors.append(error.Error('unknown function {}'.format(utilities.quote(entity.value)), entity.line, entity.column))
                arity = None

        return arity

    def _make_call_node(self, entity, arguments):
        if len(arguments) == 0:
            return entity

        name_node = ast_node.AstNode('name', value=entity.value)
        argument_list_node = ast_node.AstNode('argument_list', children=arguments)
        call_node = ast_node.AstNode('call', children=[name_node, argument_list_node])
        return call_node

    def _make_closure_node(self, call):
        return ast_node.AstNode('closure')

if __name__ == '__main__':
    import read_code
    import lexer
    import preparser

    FUNCTIONS = {'~': 1, '+': 2}

    code = read_code.read_code()
    specific_lexer = lexer.Lexer()
    specific_preparser = preparser.Preparser(specific_lexer)
    preast = specific_preparser.preparse(code)
    parser = Parser(FUNCTIONS)
    ast = parser.parse(preast)
    print(ast)

    for some_error in specific_lexer.get_errors() + specific_preparser.get_errors() + parser.get_errors():
        print(some_error)
