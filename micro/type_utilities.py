import function_type
import list_utilities

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

def combine(value_1, value_2):
    result = ''
    if isinstance(value_1, float) and isinstance(value_2, float):
        result = value_1 + value_2
    elif is_list(value_1) and is_list(value_2):
        result = list_utilities.reduce_list(
            list_utilities.map_list(value_1),
            base_pair=value_2,
        )
    elif isinstance(value_1, dict) and isinstance(value_2, dict):
        result = {**value_1, **value_2}
    else:
        raise Exception(
            'unable to combine types {} and {}'.format(
                value_1.__class__.__name__,
                value_2.__class__.__name__,
            ),
        )

    return result

def _match_tuple(value, allowed_lengths):
    return isinstance(value, tuple) and len(value) in allowed_lengths
