import ply.yacc

from . import ast_node
from . import ast_token
from . import error

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
        _set_offset(node)

    @_rule('entity : HEXADECIMAL_NUMBER')
    def p_entity_hexadecimal_number(self, node):
        _process_alias('HEXADECIMAL_NUMBER', node)
        _set_offset(node)

    @_rule('entity : REAL_NUMBER')
    def p_entity_real_number(self, node):
        _process_alias('REAL_NUMBER', node)
        _set_offset(node)

    @_rule('entity : CHARACTER')
    def p_entity_character(self, node):
        _process_alias('CHARACTER', node)
        _set_offset(node)

    @_rule('entity : STRING')
    def p_entity_string(self, node):
        _process_alias('STRING', node)
        _set_offset(node)

    @_rule('entity : IDENTIFIER')
    def p_entity_identifier(self, node):
        _process_alias('IDENTIFIER', node)
        _set_offset(node)

    @_rule('entity : function')
    def p_entity_function(self, node):
        _process_equivalence(node)

    @_rule('entity : assignment')
    def p_entity_assignment(self, node):
        _process_equivalence(node)

    @_rule('entity : cast')
    def p_entity_cast(self, node):
        _process_equivalence(node)

    @_rule("function : function_declaration entity_list ';'")
    def p_function(self, node):
        _process_children_set('function', node)
        _set_offset(node, from_child=True)

    @_rule("function_declaration : \
        FUNCTION function_name '(' argument_list ')' result")
    def p_function_declaration(self, node):
        _process_children_set('function_declaration', node, [2, 4, 6])
        _set_offset(node)

    @_rule('''function_name :
        | IDENTIFIER''')
    def p_function_name(self, node):
        _process_alias('name', node)

    @_rule('''argument_list :
        | argument_list argument''')
    def p_argument_list(self, node):
        _process_list('argument_list', node)

    @_rule('argument : argument_name type')
    def p_argument(self, node):
        _process_children_set('argument', node)

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
        _process_children_set('result', node, [1])

    @_rule("assignment : assignment_declaration entity_list ';'")
    def p_assignment(self, node):
        _process_children_set('assignment', node)
        _set_offset(node, from_child=True)

    @_rule("assignment_declaration : ASSIGNMENT function_name type")
    def p_assignment_declaration(self, node):
        _process_children_set('assignment_declaration', node, [2, 3])
        _set_offset(node)

    @_rule("cast : CAST '(' entity_list ')' type")
    def p_cast(self, node):
        _process_children_set('cast', node, [3, 5])
        _set_offset(node)

    def p_error(self, token):
        if token is not None:
            self._errors.append(
                error.Error(
                    'the unexpected token {}'.format(ast_token.AstToken(token)),
                    token.lexpos,
                ),
            )

            self._preparser.errok()
        else:
            self._errors.append(
                error.Error('the unexpected token EOF', len(self._code)),
            )

def _process_list(name, node):
    items = []
    if len(node) > 1:
        if node[1] is not None:
            items = node[1].children + [node[2]]
        else:
            items = [node[2]]

    node[0] = ast_node.AstNode(name, children=items)

def _process_alias(name, node, item=1):
    node[0] = ast_node.AstNode(
        name,
        value=node[item] if len(node) > item else '',
    )

def _set_offset(node, from_child=False):
    offset = 0
    if not from_child:
        offset = node.lexpos(1)
    else:
        offset = node[0].children[0].offset

    node[0].set_offset(offset)

def _process_equivalence(node):
    node[0] = node[1]

def _process_children_set(name, node, children_numbers=[1, 2]):
    node[0] = ast_node.AstNode(
        name,
        children=[node[i] for i in children_numbers],
    )
