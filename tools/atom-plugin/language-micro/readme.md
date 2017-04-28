# language-micro package

Micro language support in Atom.

## Features

* a syntax highlighting;
* editor settings:
	* a comment start;
	* indent patterns;
* snippets.

## Snippets

Prefix | Body
--- | ---
fn | a function declaration
le | an assignment
as | a cast
if | a condition (a call of `if` function)
> | a packing (a call of `>@` function with a function declaration)
< | an unpacking (a call of `<<@` function)
, | a list construction (a call of `,` function with `[]` as a second argument)
. | a hash getter (a call of `.` function with a string first argument)
\# | a hash setter (a call of `#` function with a string first argument)

## License

The MIT License (MIT)

Copyright &copy; 2016, 2017 thewizardplusplus
