import json

class AstNode:
    def __init__(self, name, value=None, children=None):
        self.name = name
        if value is not None:
            self.value = value
        if children is not None:
            self.children = children

    def __str__(self):
        return json.dumps(self, cls=AstNodeEncoder)

    def set_offset(self, offset):
        self.offset = offset

class AstNodeEncoder(json.JSONEncoder):
    def default(self, some_object):
        if not isinstance(some_object, AstNode):
            return super(AstNodeEncoder, self).default(some_object)

        return {
            key: some_object.__dict__[key]
            for key in some_object.__dict__.keys()
            if key != 'offset'
        }
