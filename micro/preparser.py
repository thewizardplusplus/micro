import ply.yacc
import preparser_utilities
import utilities
import ast_node
import ast_token
import error

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

    @preparser_utilities.rule('''entity_list :
        | entity_list entity''')
    def p_entity_list(self, node):
        preparser_utilities.process_list('entity_list', node)

    @preparser_utilities.rule('entity : INTEGRAL_NUMBER')
    def p_entity_integral_number(self, node):
        preparser_utilities.process_alias('INTEGRAL_NUMBER', node)

    @preparser_utilities.rule('entity : REAL_NUMBER')
    def p_entity_real_number(self, node):
        preparser_utilities.process_alias('REAL_NUMBER', node)

    @preparser_utilities.rule('entity : CHARACTER')
    def p_entity_character(self, node):
        preparser_utilities.process_alias('CHARACTER', node)

    @preparser_utilities.rule('entity : STRING')
    def p_entity_string(self, node):
        preparser_utilities.process_alias('STRING', node)

    @preparser_utilities.rule('entity : IDENTIFIER')
    def p_entity_identifier(self, node):
        preparser_utilities.process_alias('IDENTIFIER', node)
        node[0].set_position(node.lineno(1), utilities.find_column(self._code, node.lexpos(1)))

    @preparser_utilities.rule('entity : function')
    def p_entity_function(self, node):
        node[0] = node[1]

    @preparser_utilities.rule("entity : '^'")
    def p_entity_closure(self, node):
        node[0] = ast_node.AstNode('closure_mark')

    @preparser_utilities.rule("function : function_declaration entity_list ';'")
    def p_function(self, node):
        node[0] = ast_node.AstNode('function', children=[node[1], node[2]])

    @preparser_utilities.rule("function_declaration : FUNCTION function_name '(' argument_list ')' arity")
    def p_function_declaration(self, node):
        node[0] = ast_node.AstNode('function_declaration', children=[node[2], node[4], node[6]])

    @preparser_utilities.rule('function_name :')
    def p_function_name_empty(self, node):
        node[0] = ast_node.AstNode('name', value='')

    @preparser_utilities.rule('function_name : IDENTIFIER')
    def p_function_name_nonempty(self, node):
        preparser_utilities.process_alias('name', node)

    @preparser_utilities.rule('''argument_list :
        | argument_list argument''')
    def p_argument_list(self, node):
        preparser_utilities.process_list('argument_list', node)

    @preparser_utilities.rule('argument : argument_name arity')
    def p_argument(self, node):
        node[0] = ast_node.AstNode('argument', children=[node[1], node[2]])

    @preparser_utilities.rule('argument_name : IDENTIFIER')
    def p_argument_name(self, node):
        preparser_utilities.process_alias('name', node)

    @preparser_utilities.rule('arity :')
    def p_arity_zero(self, node):
        node[0] = ast_node.AstNode('arity', value=0)

    @preparser_utilities.rule("arity : ':' INTEGRAL_NUMBER")
    def p_arity_nonzero(self, node):
        node[0] = ast_node.AstNode('arity', value=node[2])

    def p_error(self, token):
        if not token is None:
            self._errors.append(error.Error('unexpected token {}'.format(ast_token.AstToken(token)), token.lineno, utilities.find_column(self._code, token.lexpos)))
            self._preparser.errok()
        else:
            self._errors.append(error.Error('unexpected token EOF', self._code.count('\n') + 1, utilities.find_column(self._code, len(self._code))))            

if __name__ == '__main__':
    import read_code
    import lexer

    code = read_code.read_code()
    specific_lexer = lexer.Lexer()
    preparser = Preparser(specific_lexer)
    preast = preparser.preparse(code)
    print(preast)

    for some_error in specific_lexer.get_errors() + preparser.get_errors():
        print(some_error)
