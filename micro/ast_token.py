import ast_token_encoder
import json

class AstToken:
    def __init__(self, lex_token):
        self.name = lex_token.type
        if lex_token.value != self.name:
            self.value = lex_token.value

    def __str__(self):
        return json.dumps(self, cls=ast_token_encoder.AstTokenEncoder)
