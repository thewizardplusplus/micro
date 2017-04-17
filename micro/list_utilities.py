import functools

def reduce_list(some_list, handler=None):
    return functools.reduce(
        lambda pair, item: (item, pair),
        (_handle_item(item, handler) for item in reversed(some_list)),
        (),
    )

def map_list(some_pair, handler=None):
    items = []
    while len(some_pair) > 0:
        item, some_pair = some_pair
        items.append(_handle_item(item, handler))

    return items

def _handle_item(item, handler):
    return handler(item) if handler is not None else item
