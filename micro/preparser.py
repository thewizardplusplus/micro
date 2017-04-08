import ply.yacc
import ast_node
import ast_token
import error

def _rule(grammar):
    def set_doc(function):
        function.__doc__ = grammar
        return function

    return set_doc

class Preparser:
    _errors = []

    def __init__(self, lexer):
        self.tokens = lexer.tokens
        self._lexer = lexer
        self._preparser = ply.yacc.yacc(module=self, debug=False)

    def preparse(self, code):
        self._code = code
        return self._preparser.parse(code, lexer=self._lexer)

    def get_errors(self):
        return self._errors

    @_rule('''entity_list :
        | entity_list entity''')
    def p_entity_list(self, node):
        _process_list('entity_list', node)

    @_rule('entity : INTEGRAL_NUMBER')
    def p_entity_integral_number(self, node):
        _process_alias('INTEGRAL_NUMBER', node)

    @_rule('entity : REAL_NUMBER')
    def p_entity_real_number(self, node):
        _process_alias('REAL_NUMBER', node)

    @_rule('entity : CHARACTER')
    def p_entity_character(self, node):
        _process_alias('CHARACTER', node)

    @_rule('entity : STRING')
    def p_entity_string(self, node):
        _process_alias('STRING', node)

    @_rule('entity : IDENTIFIER')
    def p_entity_identifier(self, node):
        _process_alias('IDENTIFIER', node)
        node[0].set_offset(node.lexpos(1))

    @_rule('entity : function')
    def p_entity_function(self, node):
        node[0] = node[1]

    @_rule('entity : assignment')
    def p_entity_assignment(self, node):
        node[0] = node[1]

    @_rule("function : function_declaration entity_list ';'")
    def p_function(self, node):
        node[0] = ast_node.AstNode('function', children=[node[1], node[2]])

    @_rule("function_declaration : FUNCTION function_name '(' argument_list ')' result")
    def p_function_declaration(self, node):
        node[0] = ast_node.AstNode('function_declaration', children=[node[2], node[4], node[6]])

    @_rule('function_name :')
    def p_function_name_empty(self, node):
        node[0] = ast_node.AstNode('name', value='')

    @_rule('function_name : IDENTIFIER')
    def p_function_name_nonempty(self, node):
        _process_alias('name', node)

    @_rule('''argument_list :
        | argument_list argument''')
    def p_argument_list(self, node):
        _process_list('argument_list', node)

    @_rule('argument : argument_name type')
    def p_argument(self, node):
        node[0] = ast_node.AstNode('argument', children=[node[1], node[2]])

    @_rule('argument_name : IDENTIFIER')
    def p_argument_name(self, node):
        _process_alias('name', node)

    @_rule('''type :
        | type arity''')
    def p_type(self, node):
        _process_list('type', node)

    @_rule("arity : ':' INTEGRAL_NUMBER")
    def p_arity(self, node):
        _process_alias('arity', node, 2)

    @_rule('result : type')
    def p_result(self, node):
        node[0] = ast_node.AstNode('result', children=[node[1]])

    @_rule("assignment : assignment_declaration entity_list ';'")
    def p_assignment(self, node):
        node[0] = ast_node.AstNode('assignment', children=[node[1], node[2]])

    @_rule("assignment_declaration : ASSIGNMENT function_name type")
    def p_assignment_declaration(self, node):
        node[0] = ast_node.AstNode('assignment_declaration', children=[node[2], node[3]])

    def p_error(self, token):
        if token is not None:
            self._errors.append(error.Error('the unexpected token {}'.format(ast_token.AstToken(token)), token.lexpos))
            self._preparser.errok()
        else:
            self._errors.append(error.Error('the unexpected token EOF', len(self._code)))

def _process_list(name, node):
    items = []
    if len(node) > 1:
        if node[1] is not None:
            items = node[1].children + [node[2]]
        else:
            items = [node[2]]

    node[0] = ast_node.AstNode(name, children=items)

def _process_alias(name, node, item=1):
    node[0] = ast_node.AstNode(name, value=node[item])

if __name__ == '__main__':
    import read_code
    import lexer

    code = read_code.read_code()
    specific_lexer = lexer.Lexer()
    preparser = Preparser(specific_lexer)
    preast = preparser.preparse(code)
    print(preast)

    for some_error in specific_lexer.get_errors() + preparser.get_errors():
        some_error.detect_position(code)
        print(some_error)
