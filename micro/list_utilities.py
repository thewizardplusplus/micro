import functools

def reduce_list(some_list, handler=None, base_pair=()):
    return functools.reduce(
        lambda pair, item: (item, pair),
        (_handle_item(item, handler) for item in reversed(some_list)),
        base_pair,
    )

def map_list(some_pair, handler=None, base_list=[]):
    items = [*base_list]
    while len(some_pair) > 0:
        item, some_pair = some_pair
        items.append(_handle_item(item, handler))

    return items

def concatenate(pair_1, pair_2):
    return reduce_list(map_list(pair_1), base_pair=pair_2)

def _handle_item(item, handler):
    return handler(item) if handler is not None else item
