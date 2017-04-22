import type_utilities

def closure_trampoline(value):
    while type_utilities.is_nullary_closure(value):
        value = value()

    return value

def pack_trampoline(value):
    while type_utilities.is_pack(value):
        value = closure_trampoline(value[0])

    return value
