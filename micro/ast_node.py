import ast_node_encoder
import json

class AstNode:
    def __init__(self, name, value=None, children=None):
        self.name = name
        if value is not None:
            self.value = value
        if children is not None:
            self.children = children

    def __str__(self):
        return json.dumps(self, cls=ast_node_encoder.AstNodeEncoder)

    def set_offset(self, offset):
        self.offset = offset
