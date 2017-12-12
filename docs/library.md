### ![](logo/logo.png) Библиотека

* функции для работы с CLI:
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
			* `"white"`;
* функции для работы со списками:
	* `generate(number: num, generator: any|closure(): any): list<any>`;
	* `for_each(list: list<any>, handler: closure(item: any): nil): nil`;
	* `map(list: list<any>, handler: closure(item: any): any): list<any>`;
	* `reduce(list: list<any>, initial: any, handler: closure(result: any, item: any): any): any`;
	* `zip(list_i: list<any>, list_ii: list<any>, handler: closure(item_i: any, item_ii: any): any): list<any>`;
	* `reverse(list: list<any>): list<any>`;
	* `last(list: list<any>): any`;
	* `count(list: list<any>, item: any): num`;
	* `find(list: list<any>, comparator: closure(item: any): bool): nil|num`;
* функции для юнит-тестирования:
	* `test(name: str, test: closure(): bool): bool`;
	* `group(name: str, tests: closure(): list<bool>): list<bool>`.
