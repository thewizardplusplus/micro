### Grammar

```
program = entity list;

entity list = {entity};
entity = INTEGRAL NUMBER
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

SINGLE-LINE COMMENT = ? /(?<![a-z_])nb(?![:a-z_]).*/i ?;
MULTILINE COMMENT = ? /(?<![a-z_])nb:.*?(?<![a-z_])nb;/is ?;
INTEGRAL NUMBER = ? /\d+/ ?;
REAL NUMBER = ? /\d+(((\.\d+)(e-?\d+))|(\.\d+)|(e-?\d+))/ ?;
CHARACTER = ? /'(\\.|[^'])'/ ?;
STRING = ? /"(\\.|[^"])*"/ ?;
ALPHABETIC IDENTIFIER = ? /[a-z_]+/i ?;
PUNCTUATION IDENTIFIER = ? /[!#$%&*+,\-.\/<=>?@[\\\]^`{|}~]+/ ?;
```
