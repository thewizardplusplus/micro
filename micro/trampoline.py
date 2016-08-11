import type_utilities

def closure_trampoline(value):
    while type_utilities.is_closure(value):
        value = value()

    return value

def make_closure_trampoline_wrapper(handler):
    return lambda *args: handler(*[closure_trampoline(arg) for arg in args])

@make_closure_trampoline_wrapper
def pack_trampoline(value):
    while type_utilities.is_pack(value):
        value = closure_trampoline(value[0])

    return value
