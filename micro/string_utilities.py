import functools

def make_list_from_string(string):
    return functools.reduce(lambda pair, character: (character, pair), map(ord, reversed(string)), ())

def make_string_from_list(pair):
    items = _map_list(pair, chr)
    return ''.join(items)

def get_representation(value):
    return str(value) if not _is_list(value) else _get_list_representation(value)

def _map_list(pair, handler):
    items = []
    while len(pair) > 0:
        item = handler(pair[0])
        items.append(item)

        pair = pair[1]

    return items

# it shouldn't be recursive
def _is_list(value):
    return (isinstance(value, tuple)
        # it's used to distinguish the list ​​from the pack
        and (len(value) == 0 or len(value) == 2))

def _get_list_representation(pair):
    items = _map_list(pair, get_representation)
    return '[' + ', '.join(items) + ']'
