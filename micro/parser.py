import ast_node
import utilities
import error

class Parser:
    _errors = []

    def __init__(self, functions={}):
        self._functions = functions

    def parse(self, preast):
        preast.children = self._make_call_list(preast.children, self._functions)
        return preast

    def get_errors(self):
        return self._errors

    def _make_call_list(self, entities, functions):
        calls = []
        while len(entities) > 0:
            call, entities = self._make_call(entities[0], entities[1:], functions)
            if call is None:
                continue
            if call.name == 'function':
                call.children[1].children = self._make_call_list(call.children[1].children, functions)
            if call.name == 'call' and call.children[1].children[-1].name == 'closure_mark':
                call.children[1].children.pop()
                call = self._make_closure_node(call, functions)

            calls.append(call)

        return calls

    def _make_call(self, first_entity, rest_entities, functions):
        arity = self._get_arity(first_entity, functions)
        if arity is None:
            return None, rest_entities

        arguments = []
        while arity > 0 and len(rest_entities) > 0:
            call, rest_entities = self._make_call(rest_entities[0], rest_entities[1:], functions)
            if call is None:
                continue
            if call.name == 'closure_mark':
                break

            arguments.append(call)
            arity -= 1

        if arity > 0:
            arguments.append(ast_node.AstNode('closure_mark'))

        if len(arguments) == 0:
            return first_entity, rest_entities
        else:
            call = self._make_call_node(first_entity, arguments)
            return self._make_call(call, rest_entities, functions)

    def _get_arity(self, entity, functions):
        arity = 0
        if entity.name == 'IDENTIFIER':
            if entity.value in self._functions:
                arity = functions[entity.value]
            else:
                self._errors.append(error.Error('unknown function {}'.format(utilities.quote(entity.value)), entity.offset))
                arity = None
        elif entity.name == 'call':
            pass

        return arity

    def _make_call_node(self, function, arguments):
        inner_call_node = ast_node.AstNode('inner_call', children=[function])
        result_node = self._make_result_node(0)
        inner_function_node = ast_node.AstNode('inner_function', children=[inner_call_node, result_node])
        arguments_node = ast_node.AstNode('argument_list', children=arguments)
        return ast_node.AstNode('call', children=[inner_function_node, arguments_node])

    def _make_closure_node(self, call, functions):
        arguments_names = self._get_closure_arguments_names(call, functions)
        closure_declaration_node = self._make_closure_declaration_node(arguments_names)
        closure_body_node = self._make_closure_body_node(call, arguments_names)
        return ast_node.AstNode('function', children=[closure_declaration_node, closure_body_node])

    def _get_closure_arguments_names(self, call, functions):
        call_arity = functions[call.children[0].value]
        closure_arity = call_arity - len(call.children[1].children)
        return ['_{}'.format(i) for i in range(closure_arity)]

    def _make_closure_declaration_node(self, arguments_names):
        name_node = ast_node.AstNode('name', value='')
        arguments_node = self._make_closure_arguments_node(arguments_names)
        result_node = self._make_closure_result_node(len(arguments_names))
        return ast_node.AstNode('function_declaration', children=[name_node, arguments_node, result_node])

    def _make_closure_arguments_node(self, arguments_names):
        arguments_names_nodes = [ast_node.AstNode('name', value=argument_name) for argument_name in arguments_names]
        arguments_arities_nodes = [ast_node.AstNode('arity', value=0)] * len(arguments_names)
        arguments_nodes = [ast_node.AstNode('argument', children=list(argument)) for argument in zip(arguments_names_nodes, arguments_arities_nodes)]
        return ast_node.AstNode('argument_list', children=arguments_nodes)

    def _make_result_node(self, arity):
        arity_node = ast_node.AstNode('arity', value=arity)
        return ast_node.AstNode('result', children=[arity_node])

    def _make_closure_body_node(self, call, arguments_names):
        arguments_nodes = [ast_node.AstNode('IDENTIFIER', value=argument_name) for argument_name in arguments_names]
        call.children[1].children.extend(arguments_nodes)
        return ast_node.AstNode('entity_list', children=[call])

if __name__ == '__main__':
    import function_type
    import read_code
    import lexer
    import preparser

    FUNCTIONS = {
        '~': function_type.FunctionType(1),
        '+': function_type.FunctionType(2),
        'rand': function_type.FunctionType(1, function_type.FunctionType(1, function_type.FunctionType(1)))
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
