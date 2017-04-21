import utilities

@utilities.make_arguments_processor(int)
def bitwise_and(number_1, number_2):
    return float(number_1 & number_2)

@utilities.make_arguments_processor(int)
def bitwise_or(number_1, number_2):
    return float(number_1 | number_2)

@utilities.make_arguments_processor(int)
def bitwise_xor(number_1, number_2):
    return float(number_1 ^ number_2)

@utilities.make_arguments_processor(int)
def bitwise_left_shift(number_1, number_2):
    return float(number_1 << number_2)

@utilities.make_arguments_processor(int)
def bitwise_arithmetic_right_shift(number_1, number_2):
    return float(number_1 >> number_2)

@utilities.make_arguments_processor(int)
def bitwise_logical_right_shift(number_1, number_2):
    # the modulo operator always yields a result with the same sign as its
    # second operand
    return float((number_1 % (1 << 32)) >> number_2)

@utilities.make_arguments_processor(int)
def bitwise_not(number):
    return float(~number)
