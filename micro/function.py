from re import sub

class function:
    def __init__(self, handle, arguments=None, arity=None, body=[]):
        self.handle = handle
        self.arguments = arguments
        self.body = body

        if arguments is not None:
            self.arity = len(arguments)
        elif arity is not None:
            self.arity = arity

            self.arguments = []
            for i in range(arity):
                argument = '_{:d}'.format(i)
                self.arguments.append(argument)
        else:
            raise Exception('invalid arguments of function.__init__')

    def __repr__(self):
        body = ' '.join(self.body) if self.body else '[unknown]'

        body = sub(r'\s?(\(|\))\s?', r'\1', body)
        body = sub(r"\s(;|')", r'\1', body)
        body = sub("';", ';', body)
        body = sub(r'^fn\(\)(.*);$', r'\1', body)

        arguments = ' '.join(self.arguments)
        return 'fn({:s}){:s};'.format(arguments, body)
