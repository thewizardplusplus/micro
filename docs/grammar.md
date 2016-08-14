### Grammar

```
program = entity list;

entity list = {entity};
entity = INTEGRAL NUMBER
	| REAL NUMBER
	| CHARACTER
	| STRING
	| identifier
	| function definition
	| function call;
identifier = (ALPHABETIC IDENTIFIER - "fn") | PUNCTUATION IDENTIFIER;
function definition = "fn", [identifier], "(", {identifier, type}, ")", type,
		entity list,
	";";
type = {":", INTEGRAL NUMBER};
function call = entity, entity, {entity};

SINGLE-LINE COMMENT = ? /(?<![a-z_])nb(?![:a-z_]).*/i ?;
MULTILINE COMMENT = ? /(?<![a-z_])nb:.*?(?<![a-z_])nb;/is ?;
INTEGRAL NUMBER = ? /\d+/ ?;
REAL NUMBER = ? /\d+(((\.\d+)(e-?\d+))|(\.\d+)|(e-?\d+))/ ?;
CHARACTER = ? /'(\\['\\tn]|[^'\n])'/ ?;
STRING = ? /"(\\["\\tn]|(?!\\)[^"])*"/ ?;
ALPHABETIC IDENTIFIER = ? /[a-z_]+/i ?;
PUNCTUATION IDENTIFIER = ? /[!#$%&*+,\-.\/<=>?@[\\\]^`{|}~]+/ ?;
```
