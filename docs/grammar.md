### Grammar

```
program = entity list;

entity list = {entity};
entity = INTEGRAL NUMBER
	| HEXADECIMAL NUMBER
	| REAL NUMBER
	| CHARACTER
	| STRING
	| identifier
	| assignment
	| cast
	| function definition
	| function call;
key words = "fn" | "let" | "as";
identifier = (ALPHABETIC IDENTIFIER - key words) | PUNCTUATION IDENTIFIER;
assignment = "let", [identifier], type,
		entity list,
	";";
cast = "as", "(", entity list, ")", type;
function definition = "fn", [identifier], "(", {identifier, type}, ")", type,
		entity list,
	";";
type = {":", INTEGRAL NUMBER};
function call = entity, entity, {entity};

SINGLE-LINE COMMENT = ? /(?<![A-Za-z_])nb(?![:A-Za-z_]).*/ ?;
MULTILINE COMMENT = ? /(?<![A-Za-z_])nb:.*?(?<![A-Za-z_])nb;/s ?;
INTEGRAL NUMBER = ? /\d+/ ?;
HEXADECIMAL NUMBER = ? /0x[A-Fa-f0-9]+/ ?;
REAL NUMBER = ? /\d+(((\.\d+)(e-?\d+))|(\.\d+)|(e-?\d+))/ ?;
CHARACTER = ? /'(\\.|\\x[A-Fa-f0-9]{2}|[^'])'/ ?;
STRING = ? /"(\\.|\\x[A-Fa-f0-9]{2}|[^"])*"/ ?;
ALPHABETIC IDENTIFIER = ? /[a-z_]+/i ?;
PUNCTUATION IDENTIFIER = ? /[!#$%&*+,\-.\/<=>?@[\\\]^`{|}~]+/ ?;
```
