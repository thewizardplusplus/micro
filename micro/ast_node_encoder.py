import json
import ast_node

class AstNodeEncoder(json.JSONEncoder):
    def default(self, some_object):
        if not isinstance(some_object, ast_node.AstNode):
            return super(AstNodeEncoder, self).default(some_object)

        return {key: some_object.__dict__[key] for key in some_object.__dict__.keys() if not key in ['line', 'column']}
