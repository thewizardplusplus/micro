CODE = '''
fn outln(value)
    out str value
    out "\n"
;

outln + 2 3

fn add(x y) + x y;
outln add 2 3

fn app(op:2 x y) op x y;
outln app fn(x y) + x y; 2 3

fn add(x):1 fn(y) + x y;;
outln add 2 3

fn ans() fn() 42;;
outln ans

fn add():0:2 fn():2 fn(x y) fn() + 2 3;;;;
outln add 2 3

fn loop(limit)
    fn _loop(counter limit)
        if < counter limit
            fn()
                out "\r"
                out str counter

                |>fn() _loop + 1 counter limit;
            ;
            fn();
    ;

    @_loop 0 limit
    out "\n"
;
loop 2000
'''

if __name__ == '__main__':
    import lexer
    import preparser
    import parser
    import builtin_functions
    import sys
    import evaluate

    specific_lexer = lexer.Lexer()
    specific_preparser = preparser.Preparser(specific_lexer)
    preast = specific_preparser.preparse(CODE)
    specific_parser = parser.Parser()
    ast = specific_parser.parse(preast, builtin_functions.BUILTIN_FUNCTIONS)
    errors = specific_lexer.get_errors() + specific_preparser.get_errors() + specific_parser.get_errors()
    for some_error in errors:
        some_error.detect_position(CODE)
        print(some_error)
    if errors:
        sys.exit()

    evaluate.evaluate(ast, builtin_functions.BUILTIN_FUNCTIONS)
