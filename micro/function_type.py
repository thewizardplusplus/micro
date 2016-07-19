class FunctionType:
    def __init__(self, arity=0, result=None):
        self.arity = arity
        self.result = result

    def to_ast(self):
        arities = self.to_array()
        pass

    def to_array(self):
        return _simplify_type(self._to_raw_array())

    def _to_raw_array(self):
        return [self.arity] + (self.result._to_raw_array() if self.result is not None else [])

def make_type_from_array(arities):
    return _simplify_type(_make_type_from_raw_array(arities))

def _simplify_type(arities):
    first_nonzero = next((index for index, arity in zip(range(len(arities), 0, -1), reversed(arities)) if arity != 0), -1)
    if first_nonzero == -1:
        return []

    return arities[:first_nonzero]

def _make_type_from_raw_array(arities):
    if len(arities) == 0:
        return FunctionType(0)

    return FunctionType(arities[0], _make_type_from_raw_array(arities[1:]))
