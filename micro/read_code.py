import fileinput

def read_code(filename='-'):
    return ''.join(line for line in fileinput.input(filename))
