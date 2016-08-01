import functools

def string_to_list(string):
    return functools.reduce(lambda pair, character: (character, pair), map(ord, reversed(string)), ())

def string_from_list(pair):
    characters = []
    while len(pair) > 0:
        characters.append(pair[0])
        pair = pair[1]

    return ''.join(map(chr, characters))
