### Рантайм

* общие функции:
	* `==(x: any, y: any): bool` &mdash; равенство;
	* `!=(x: any, y: any): bool` &mdash; неравенство;
	* `!(x: any): bool` &mdash; логическое отрицание;
	* `&&(x: any, y: any): bool` &mdash; конъюнкция;
	* `||(x: any, y: any): bool` &mdash; дизъюнкция;
	* `if(condition: bool, true_value: any, false_value: any): bool` &mdash; выбор: если `condition` истинно, возвращает `true_value`, иначе &mdash; `false_value`;
	* функции для работы с типами:
		* `nil(): nil` &mdash; возвращает значение нулевого типа;
		* `false(): bool` &mdash; возвращает ложное логическое значение (число 0);
		* `true(): bool` &mdash; возвращает истинное логическое значение (число 1);
		* `num(x: str): num` &mdash; парсит число из строки;
		* `type(x: any): str` &mdash; возвращает имя типа переданного значения;
		* `arity(x: closure): list<num>` &mdash; возвращает список арностей переданного замыкания (голова списка &mdash; арность самого замыкания, хвост &mdash; аналогичный список для результата замыкания);
		* `str(x: any): str` &mdash; преобразует переданное значение в строку;
		* `strb(x: bool): str` &mdash; преобразует переданное логическое значение в строку: если `x` истинно, возвращает `"true"`, иначе &mdash; `"false"`;
		* `strl(x: list<str>): str` &mdash; преобразует переданный список строк в строку, отображая при этом строки как строки;
* числовые функции:
	* `<(x: num, y: num): bool` &mdash; меньше;
	* `<=(x: num, y: num): bool` &mdash; меньше или равно;
	* `>(x: num, y: num): bool` &mdash; больше;
	* `>=(x: num, y: num): bool` &mdash; больше или равно;
	* `~(x: num): num` &mdash; унарный минус;
	* `+(x: num, y: num): num` &mdash; сложение;
	* `-(x: num, y: num): num` &mdash; вычитание;
	* `*(x: num, y: num): num` &mdash; умножение;
	* `/(x: num, y: num): num` &mdash; деление;
	* `%(x: num, y: num): num` &mdash; остаток от деления;
	* математические функции:
		* `floor(x: num): num`;
		* `ceil(x: num): num`;
		* `trunc(x: num): num`;
		* `round(x: num): num`;
		* `sin(x: num): num`;
		* `cos(x: num): num`;
		* `tn(x: num): num`;
		* `arcsin(x: num): num`;
		* `arccos(x: num): num`;
		* `arctn(x: num): num`;
		* `angle(y: num, x: num): num` &mdash; atan2;
		* `pow(base: num, exponent: num): num`;
		* `sqrt(x: num): num`;
		* `exp(x: num): num`;
		* `ln(x: num): num`;
		* `lg(x: num): num`;
		* `abs(x: num): num`;
		* `random(): num` &mdash; возвращает случайное число в диапазоне [0; 1);
* функции для работы со списками:
	* `[](): list<any>` &mdash; возвращает пустой список;
	* `,(head: any, tail: list<any>): list<any>` &mdash; конструирует новый список из переданных головы и хвоста;
	* `head(list: list<any>): any` &mdash; возвращает голову списка;
	* `tail(list: list<any>): list<any>` &mdash; возвращает хвост списка;
* функции для упаковки:
	* `>@(x: any): pack<any>` &mdash; упаковывает переданное значение без его предварительного вычисления;
	* `<@(x: pack<any>): any` &mdash; распаковывает переданное значение;
	* `<<@(x: pack<any>): any` &mdash; распаковывает переданное значение в цикле до тех пор, пока результат является упакованным значением;
* системные функции:
	* `env(name: str): str|nil` &mdash; возвращает значение указанной переменной окружения, если она установлена; в противном случае возвращается `nil`;
	* `time(): num` &mdash; возвращает текущее UNIX-время по UTC;
	* `exit(code: num): nil` &mdash; завершает программу с переданным кодом возврата;
	* функции для ввода/вывода:
		* `in(number: nil|num): str` &mdash; считывает указанное количество символов из stdin и возвращает их в виде строки; если вместо количества будет передан `nil`, то будут считаны все доступные в stdin символы;
		* `out(string: str): nil` &mdash; выводит переданную строку в stdout;
		* `outln(string: str): nil` &mdash; выводит переданную строку в stdout и переводит строку (добавляет символ `'\n'`);
		* `err(string: str): nil` &mdash; выводит переданную строку в stderr;
		* `errln(string: str): nil` &mdash; выводит переданную строку в stderr и переводит строку (добавляет символ `'\n'`).
