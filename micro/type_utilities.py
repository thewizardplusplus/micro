import function_type

# it shouldn't be recursive
def is_list(value):
    return _match_tuple(value, [0, 2])

def is_pack(value):
    return _match_tuple(value, [1])

def is_closure(value):
    return isinstance(value, function_type.FunctionType)

def is_nullary_closure(value):
    return is_closure(value) and not value.is_callable()

def get_type_name(value):
    name = ''
    if value is None:
        name = 'nil'
    elif isinstance(value, float):
        name = 'num'
    elif is_list(value):
        name = 'list'
    elif isinstance(value, dict):
        name = 'hash'
    elif is_pack(value):
        name = 'pack'
    elif is_closure(value):
        name = 'closure'
    else:
        raise Exception('the unknown type {}'.format(value.__class__.__name__))

    return name

def _match_tuple(value, allowed_lengths):
    return isinstance(value, tuple) and len(value) in allowed_lengths
