### Рантайм

* общие функции:
	* `==(x: any, y: any): bool` &mdash; равенство;
	* `!=(x: any, y: any): bool` &mdash; неравенство;
	* `!(x: any): bool` &mdash; логическое отрицание;
	* `&&(x: any, y: any): bool` &mdash; конъюнкция;
	* `||(x: any, y: any): bool` &mdash; дизъюнкция;
	* `if(condition: bool, true_value: any, false_value: any): bool` &mdash; выбор:  если `condition` истинно, возвращает `true_value`, иначе &mdash; `false_value`;
	* функции для работы с типами:
		* `nil(): nil` &mdash; возвращает значение нулевого типа;
		* `num(x: str): num` &mdash; парсит вещественное число из строки;
		* `type(x: any): str` &mdash; возвращает имя типа переданного значения;
		* `arity(x: closure): list<int>` &mdash; возвращает список арностей переданного замыкания (голова списка &mdash; арность самого замыкания, хвост &mdash; аналогичный список для результата замыкания);
		* `str(x: any): str` &mdash; преобразует переданное значение в строку;
* числовые функции:
	* `<(x: int|num, y: int|num): bool` &mdash; меньше;
	* `<=(x: int|num, y: int|num): bool` &mdash; меньше или равно;
	* `>(x: int|num, y: int|num): bool` &mdash; больше;
	* `>=(x: int|num, y: int|num): bool` &mdash; больше или равно;
	* `~(x: int|num): int|num` &mdash; унарный минус;
	* `+(x: int|num, y: int|num): int|num` &mdash; сложение;
	* `-(x: int|num, y: int|num): int|num` &mdash; вычитание;
	* `*(x: int|num, y: int|num): int|num` &mdash; умножение;
	* `/(x: int|num, y: int|num): int|num` &mdash; деление (для целых чисел &mdash; целочисленное деление, для вещественных &mdash; вещественное);
	* `%(x: int|num, y: int|num): int|num` &mdash; остаток от деления (для вещественных чисел &mdash; вещественный остаток);
	* математические функции:
		* `floor(x: num): num`;
		* `ceil(x: num): num`;
		* `trunc(x: num): int`;
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
		* `random(): num` &mdash; возвращает случайное вещественное число в диапазоне [0; 1);
* функции для работы со списками:
	* `$(): list<any>` &mdash; возвращает пустой список;
	* `,(head: any, tail: list<any>): list<any>` &mdash; конструирует новый список из переданных головы и хвоста;
	* `head(list: list<any>): any` &mdash; возвращает голову списка;
	* `tail(list: list<any>): list<any>` &mdash; возвращает хвост списка;
* функции для упаковки:
	* `>@(x: any): pack<any>` &mdash; упаковывает переданное значение без его предварительного вычисления;
	* `<@(x: pack<any>): any` &mdash; распаковывает переданное значение;
	* `<<@(x: pack<any>): any` &mdash; распаковывает переданное значение в цикле до тех пор, пока результат является упакованным значением;
* системные функции:
	* `exit(code: int): nil` &mdash; завершает программу с переданным кодом возврата;
	* функции для ввода/вывода:
		* `in(): int` &mdash; считывает один символ из stdin и возвращает его код;
		* `out(string: str): nil` &mdash; выводит переданную строку в stdout;
		* `err(string: str): nil` &mdash; выводит переданную строку в stderr.
