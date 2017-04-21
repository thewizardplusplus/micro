import type_utilities
import utilities

def closure_trampoline(value):
    while type_utilities.is_nullary_closure(value):
        value = value()

    return value

def make_closure_trampoline_wrapper(function):
    return utilities.make_arguments_processor(closure_trampoline)(function)

def pack_trampoline(value):
    while type_utilities.is_pack(value):
        value = closure_trampoline(value[0])

    return value
