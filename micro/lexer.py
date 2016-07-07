import string
import re
import ply.lex
import ast_token
import lexer_utilities
import utilities
import error

class Lexer:
    _keywords = {'fn' : 'FUNCTION'}

    tokens = ['INTEGRAL_NUMBER', 'REAL_NUMBER', 'CHARACTER', 'STRING', 'IDENTIFIER'] + list(_keywords.values())
    t_ignore = ' \t'
    literals = '():;^'

    _letters = 'A-Za-z_'
    _punctuation = string.punctuation.translate({ord(character): None for character in '\'"' + literals})
    _errors = []

    def __init__(self):
        self._lexer = ply.lex.lex(module=self, reflags=re.DOTALL)

    def input(self, code):
        self._lexer.input(code)

    def token(self):
        return self._lexer.token()

    def tokenize(self, code):
        self.input(code)
        return [ast_token.AstToken(lex_token) for lex_token in self._lexer]

    def get_errors(self):
        return self._errors

    @ply.lex.TOKEN('(?<![{0}])nb(?![{0}:]).*'.format(_letters))
    def t_SINGLE_LINE_COMMENT(self, token):
        pass

    @ply.lex.TOKEN('(?<![{0}])nb:.*(?<![{0}])nb;'.format(_letters))
    def t_MULTILINE_COMMENT(self, token):
        pass

    @ply.lex.TOKEN(r'[{}]+|[{}]+'.format(_letters, re.escape(_punctuation)))
    def t_IDENTIFIER(self, token):
        if token.value in self._keywords:
            token.type = self._keywords[token.value]

        return token

    @ply.lex.TOKEN(r'\d+((\.\d+e-?\d+)|(\.\d+)|(e-?\d+))')
    def t_REAL_NUMBER(self, token):
        token.value = float(token.value)
        return token

    @ply.lex.TOKEN(r'\d+')
    def t_INTEGRAL_NUMBER(self, token):
        token.value = int(token.value)
        return token

    @ply.lex.TOKEN(r"'(\\.|[^'])'")
    def t_CHARACTER(self, token):
        token.value = lexer_utilities.extract_string(token.value)
        return token

    @ply.lex.TOKEN(r'"(\\.|[^"])*"')
    def t_STRING(self, token):
        token.value = lexer_utilities.extract_string(token.value)
        return token

    @ply.lex.TOKEN(r'\n+')
    def t_newline(self, token):
        self._lexer.lineno += len(token.value)

    def t_error(self, token):
        self._errors.append(error.Error('illegal character {}'.format(utilities.quote(token.value[0])), token.lineno, utilities.find_column(self._lexer.lexdata, token.lexpos)))
        self._lexer.skip(1)

if __name__ == '__main__':
    import read_code
    import ast_token_encoder
    import json

    code = read_code.read_code()
    lexer = Lexer()
    tokens = lexer.tokenize(code)
    print(json.dumps(tokens, cls=ast_token_encoder.AstTokenEncoder))

    for some_error in lexer.get_errors():
        print(some_error)
