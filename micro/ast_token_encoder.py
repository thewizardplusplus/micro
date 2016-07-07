import json
import ast_token

class AstTokenEncoder(json.JSONEncoder):
    def default(self, some_object):
        if not isinstance(some_object, ast_token.AstToken):
            return super(AstTokenEncoder, self).default(some_object)

        return some_object.__dict__
