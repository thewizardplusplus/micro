import ast_node

def _default_handler(*args):
    raise Exception('an attempt to call the default handler')

class FunctionType:
    def __init__(self, arity=0, result=None, handler=_default_handler):
        self.arity = arity
        self.result = result
        self.handler = handler

    def __call__(self, *args):
        return self.handler(*args)

    def is_callable(self):
        return self.arity != 0 \
            or (self.result is not None and self.result.is_callable())

    def get_result(self):
        return self.result if self.result is not None else FunctionType()

    def to_ast(self):
        return ast_node.AstNode(
            'type',
            children=[
                ast_node.AstNode('arity', value=arity)
                for arity in self.to_array()
            ],
        )

    def to_array(self):
        return _simplify_type(self._to_raw_array())

    def _to_raw_array(self):
        return [self.arity] \
            + (self.result._to_raw_array() if self.result is not None else [])

def make_type(value, handler=_default_handler):
    arities = []
    if isinstance(value, ast_node.AstNode):
        arities = [int(arity_node.value) for arity_node in value.children]
    elif isinstance(value, list):
        arities = value

    return _make_type_from_raw_array(_simplify_type(arities), handler)

def _simplify_type(arities):
    # remove trailing zero arities
    return arities[:next((
        index
        for index, arity in zip(
            range(len(arities), 0, -1),
            reversed(arities),
        )
        if arity != 0
    ), 0)]

def _make_type_from_raw_array(arities, handler=_default_handler):
    if len(arities) == 0:
        return FunctionType(handler=handler)

    return FunctionType(
        arities[0],
        _make_type_from_raw_array(arities[1:]),
        handler,
    )
