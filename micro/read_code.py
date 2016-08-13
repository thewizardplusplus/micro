import fileinput

def read_code(filename='-'):
    return ''.join([line for line in fileinput.input(filename)])

if __name__ == '__main__':
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else '-'
    code = read_code(filename)
    print(code)
