import fileinput

def read_code():
    return ''.join([line for line in fileinput.input()])

if __name__ == '__main__':
    code = read_code()
    print(code)
