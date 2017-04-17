import json

class AstToken:
    def __init__(self, lex_token):
        self.name = lex_token.type
        if lex_token.value != self.name:
            self.value = lex_token.value

    def __str__(self):
        return json.dumps(self, cls=AstTokenEncoder)

class AstTokenEncoder(json.JSONEncoder):
    def default(self, some_object):
        if not isinstance(some_object, AstToken):
            return super(AstTokenEncoder, self).default(some_object)

        return some_object.__dict__
