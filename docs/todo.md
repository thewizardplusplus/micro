### План разработки

* проверить возможности:
	* создание списка из замыканий;
	* вызов замыканий из списка;
	* возврат замыкания из функции с неверным (скалярным) типом возврата;
* добавить функции:
	* `nil():nil` &mdash; возвращает `None`;
	* `args():list<str>` &mdash; возвращает список аргументов командной строки; первый элемент списка &mdash; путь к скрипту;
	* `int(value:str):int` &mdash; парсит целое число из строки;
	* `num(value:str):num` &mdash; парсит вещественное число из строки;
	* `type(value:any):str` &mdash; возвращает имя типа переданного значения (`nil`, `int`, `num`, `list`, `pack` или `closure`);
	* `arity(value:closure):list<int>` &mdash; возвращает описание типа замыкания в виде списка арностей (`FunctionType.to_array()`);
	* математические функции:
		* `trunc(number:int|num):int`;
		* `sin(number:int|num):num`;
		* `cos(number:int|num):num`;
		* `tn(number:int|num):num`;
		* `arcsin(number:int|num):num`;
		* `arccos(number:int|num):num`;
		* `arctn(number:int|num):num`;
		* `arctn2(y:int|num, x:int|num):num`;
		* `pow(base:int|num, exponent:int|num):num`;
		* `sqrt(number:int|num):num`;
		* `exp(number:int|num):num`;
		* `ln(number:int|num):num`;
		* `lg(number:int|num):num`;
		* `abs(number:int|num):num`;
	* `in():int` &mdash; читает один символ из stdin;
	* `err(value:str):nil` &mdash; выводит строку в stderr;
	* `exit(code:int):nil` &mdash; завершает программу с указанным кодом возврата;
* добавить опции командной строки (сохранив логику загрузки скриптов):
	* `-v` или `--version`;
	* `-h` или `--help`;
	* `-t` или `--target` (`tokens`, `preast`, `ast` или `evaluation`; по умолчанию: `evaluation`);
* обновить плагин для Atom;
* обновить документацию.
