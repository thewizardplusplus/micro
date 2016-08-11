import function_type

def is_closure(value):
    return hasattr(value, '__call__') and (not isinstance(value, function_type.FunctionType) or not value.is_callable())

# it shouldn't be recursive
def is_list(value):
    return _match_tuple(value, [0, 2])

def is_pack(value):
    return _match_tuple(value, [1])

def _match_tuple(value, allowed_lengths):
    return (isinstance(value, tuple) and len(value) in allowed_lengths)
