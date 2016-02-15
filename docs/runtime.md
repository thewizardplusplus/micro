### Рантайм

* модуль `lang`:
	* `bool ==(any a, any b)`;
	* `bool !=(any a, any b)`;
	* модуль `lang.types`:
		* `nil nil()`;
		* `str type(any value)` &mdash; возвращает название типа значения
		`value`;
		* `int arity(function closure)` &mdash; возвращает арность функции;
		* `str to_str(any value)`;
		* `num to_num(str text)`;
	* модуль `lang.ops`:
		* `any if(bool condition, any true_value, any false_value)`;
		* `any while(function condition_closure, function body_closure)`;
		* `any eval(str code)`;
		* `any require(str path)`;
		* `any require_once(str path)`;
* модуль `nums`:
	* `int|num #(int|num)` &mdash; унарный минус;
	* `int|num +(int|num x, int|num y)`;
	* `int|num -(int|num x, int|num y)`;
	* `int|num *(int|num x, int|num y)`;
	* `int|num /(int|num x, int|num y)`;
	* `int %(int x, int y)`;
	* `bool <(int|num int|num)`;
	* `bool <=(int|num int|num)`;
	* `bool >(int|num int|num)`;
	* `bool >=(int|num int|num)`;
	* модуль `nums.maths`:
		* `num floor(int|num number)`;
		* `num ceil(int|num number)`;
		* `int trunc(int|num number)`;
		* `num sin(int|num number)`;
		* `num cos(int|num number)`;
		* `num tn(int|num number)`;
		* `num arcsin(int|num number)`;
		* `num arccos(int|num number)`;
		* `num arctn(int|num number)`;
		* `num arctn2(int|num y, int|num x)`;
		* `num sh(int|num number)`;
		* `num ch(int|num number)`;
		* `num th(int|num number)`;
		* `num sqrt(int|num number)`;
		* `num pow(int|num base, int|num exponent)`;
		* `num exp(int|num number)`;
		* `num ln(int|num number)`;
		* `num lg(int|num number)`;
		* `num abs(int|num number)`;
		* `num rand()` &mdash; возвращает случайное число в диапазоне [0; 1);
* модуль `bools`:
	* `bool true()`;
	* `bool false()`;
	* `any &&(any a, any b)` &mdash; если `a` соответствует `false`, возвращает
	`a`, иначе `b`;
	* `any ||(any a, any b)` &mdash; если `a` соответствует `true`, возвращает
	`a`, иначе `b`;
	* `bool !(any a)`;
* модуль `lists`:
	* `list $()` &mdash; создаёт пустой массив;
	* `list :(any value, list array)` &mdash; создаёт массив из головы `value` и
	хвоста `array`;
	* `list list(int number, any value)` &mdash; создаёт массив длиной `number`
	и заполняет его значением `value`;
	* `list append(list array, any value)`;
	* `list concat(list array_1, list array_2)`;
	* `any get(list array, int index)`;
	* `list set(list array, int index, any value)`;
	* `int len(list array)`;
* модуль `sys`:
	* `list args()` &mdash; содержит список аргументов командной строки,
	переданый скрипту; первый элемент списка содержит путь к файлу скрипта;
	* `nil exit(int code)`;
	* модуль `sys.io`:
		* `int read()` &mdash; читает 1 символ из `stdin`;
		* `str print(str text)`.
