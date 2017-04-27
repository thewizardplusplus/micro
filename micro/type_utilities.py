from . import function_type
from . import list_utilities

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
    result = None
    if isinstance(value_1, float) and isinstance(value_2, float):
        result = value_1 + value_2
    elif is_list(value_1) and is_list(value_2):
        result = list_utilities.combine_lists(value_1, value_2)
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

def get_size(value):
    size = 0.0
    if is_list(value):
        while len(value) > 0:
            _, value = value
            size += 1.0
    elif isinstance(value, dict):
        size = float(len(value))
    elif is_pack(value):
        size = 1.0
    else:
        raise Exception(
            'unable to get a size of the type {}'.format(
                value.__class__.__name__,
            ),
        )

    return size

def get_item(collection, index, default=None):
    item = default
    if is_list(collection):
        if index < 0:
            index = get_size(collection) + index

        found_item = default
        while len(collection) > 0 and index >= 0:
            found_item, collection = collection
            index -= 1

        if index == -1:
            item = found_item
    elif isinstance(collection, dict):
        item = collection.get(index, default)
    elif is_pack(collection):
        if index == 0 or index == -1:
            item = collection[0]
    else:
        raise Exception(
            'unable to get an item of the type {}'.format(
                collection.__class__.__name__,
            ),
        )

    return item

def _match_tuple(value, allowed_lengths):
    return isinstance(value, tuple) and len(value) in allowed_lengths
