### ![](logo/logo.png) Библиотека

Библиотека представлена модулем `std/`.

* `while(initial: any, checker: closure(result: any): bool, handler: closure(result: any): any): any`;
* `list/` &mdash; модуль для работы со списками:
	* `generate(initial: any, number: num, generator: closure(result: any): any): list<any>`;
	* `generate_while(initial: any, checker: closure(result: any): bool, generator: closure(result: any): any): list<any>`;
	* `for_each(list: list<any>, handler: closure(item: any): nil): nil`;
	* `map(list: list<any>, handler: closure(item: any): any): list<any>`;
	* `filter(list: list<any>, filter: closure(item: any): bool): list<any>`;
	* `reduce(list: list<any>, initial: any, handler: closure(result: any, item: any): any): any`;
	* `zip(list_i: list<any>, list_ii: list<any>, handler: closure(item_i: any, item_ii: any): any): list<any>`;
	* `zip_longest(list_i: list<any>, list_ii: list<any>, handler: closure(item_i: any, item_ii: any): any): list<any>`;
	* `reverse(list: list<any>): list<any>`;
	* `last(list: list<any>): any`;
	* `init(list: list<any>): nil|list<any>`;
	* `find(list: list<any>, comparator: closure(item: any): bool): nil|num`;
	* `find_last(list: list<any>, comparator: closure(item: any): bool): nil|num`;
	* `take(number: num, list: list<any>): list<any>`;
	* `drop(number: num, list: list<any>): list<any>`;
	* `sort(list: list<any>, lesser: closure(item_i: any, item_ii: any): bool): list<any>`;
* `cli/` &mdash; модуль для работы с CLI:
	* `ansi(name: str, text: str): str` &mdash; возвращает строку `text`, обёрнутую в [управляющую последовательность ANSI](https://ru.wikipedia.org/wiki/Управляющие_последовательности_ANSI); выбор конкретной последовательности осуществляется на основе имени `name`:
		* стили:
			* `"bold"`;
			* `"italic"`;
			* `"underline"`;
			* `"strikethrough"`;
		* цвета:
			* `"black"`;
			* `"red"`;
			* `"green"`;
			* `"yellow"`;
			* `"blue"`;
			* `"magenta"`;
			* `"cyan"`;
			* `"white"`.
