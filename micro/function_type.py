import ast_node

class FunctionType:
    def __init__(self, arity=0, result=None):
        self.arity = arity
        self.result = result

    def get_result(self):
        return self.result if self.result is not None else FunctionType(0)

    def to_ast(self):
        arities = self.to_array()
        arities_nodes = [ast_node.AstNode('arity', value=arity) for arity in arities]
        return ast_node.AstNode('type', children=arities_nodes)

    def to_array(self):
        return _simplify_type(self._to_raw_array())

    def _to_raw_array(self):
        return [self.arity] + (self.result._to_raw_array() if self.result is not None else [])

def make_type(value):
    if isinstance(value, ast_node.AstNode):
        return _make_type_from_ast(value)
    else:
        return _make_type_from_array(value)

def _simplify_type(arities):
    first_nonzero = next((index for index, arity in zip(range(len(arities), 0, -1), reversed(arities)) if arity != 0), -1)
    if first_nonzero == -1:
        return []

    return arities[:first_nonzero]

def _make_type_from_ast(type_node):
    arities = [arity_node.value for arity_node in type_node.children]
    return _make_type_from_array(arities)

def _make_type_from_array(arities):
    return _make_type_from_raw_array(_simplify_type(arities))

def _make_type_from_raw_array(arities):
    if len(arities) == 0:
        return FunctionType(0)

    return FunctionType(arities[0], _make_type_from_raw_array(arities[1:]))
