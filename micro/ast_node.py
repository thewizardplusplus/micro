import ast_node_encoder
import json

class AstNode:
    def __init__(self, name, value=None, children=None):
        self.name = name
        if not value is None:
            self.value = value
        if not children is None:
            self.children = children

    def __str__(self):
        return json.dumps(self, cls=ast_node_encoder.AstNodeEncoder)

    def set_position(self, line, column):
        self.line = line
        self.column = column
