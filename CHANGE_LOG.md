# Change Log

## [v2.1](https://github.com/thewizardplusplus/micro/tree/v2.1) (2017-04-30)

* Добавить преобразование типов [\#1](https://github.com/thewizardplusplus/micro/issues/1)
* Добавить возможность форсирования вычислений [\#2](https://github.com/thewizardplusplus/micro/issues/2)
* Удалить тип int [\#3](https://github.com/thewizardplusplus/micro/issues/3)
* Удалить внутренний тип bool [\#32](https://github.com/thewizardplusplus/micro/issues/32)
* Добавить поддержку шестнадцатеричных числовых констант [\#29](https://github.com/thewizardplusplus/micro/issues/29)
* Библиотека:
	* Добавить библиотеку для юнит-тестирования [\#53](https://github.com/thewizardplusplus/micro/issues/53)
	* Добавить библиотеку для работы со списками [\#58](https://github.com/thewizardplusplus/micro/issues/58)
	* Добавить библиотеку для работы с CLI [\#59](https://github.com/thewizardplusplus/micro/issues/59)
	* Добавить в библиотеку функцию для создания универсального цикла [\#68](https://github.com/thewizardplusplus/micro/issues/68)
* Рантайм:
	* Переименовать функцию рантайма $ в \[\] [\#4](https://github.com/thewizardplusplus/micro/issues/4)
	* Добавить в рантайм функцию round [\#10](https://github.com/thewizardplusplus/micro/issues/10)
	* Добавить в рантайм функции strb, strs, strl, strh и strhh [\#12](https://github.com/thewizardplusplus/micro/issues/12)
	* Добавить в рантайм функции false и true [\#13](https://github.com/thewizardplusplus/micro/issues/13)
	* Добавить в рантайм функции ++ и -- [\#21](https://github.com/thewizardplusplus/micro/issues/21)
	* Добавить функции рантайма + поддержку конкатенации списков и слияния хеш-таблиц [\#22](https://github.com/thewizardplusplus/micro/issues/22)
	* Добавить в рантайм битовые функции [\#30](https://github.com/thewizardplusplus/micro/issues/30)
	* Переименовать функцию рантайма ~ в \_ [\#31](https://github.com/thewizardplusplus/micro/issues/31)
	* Дополнить поддержку функции рантайма args [\#36](https://github.com/thewizardplusplus/micro/issues/36)
	* Добавить в рантайм функции для работы с хеш-таблицами [\#37](https://github.com/thewizardplusplus/micro/issues/37)
	* Добавить в рантайм функцию size [\#38](https://github.com/thewizardplusplus/micro/issues/38)
	* Сделать функции рантайма && и || ленивыми [\#46](https://github.com/thewizardplusplus/micro/issues/46)
	* Добавить в рантайм функцию load [\#49](https://github.com/thewizardplusplus/micro/issues/49)
	* Добавить в рантайм функцию для доступа к коллекциям по индексу [\#60](https://github.com/thewizardplusplus/micro/issues/60)
	* Добавить в функции рантайма head и tail поддержку пустых списков [\#61](https://github.com/thewizardplusplus/micro/issues/61)
	* Добавить в рантайм функцию для указания значений по умолчанию [\#62](https://github.com/thewizardplusplus/micro/issues/62)
	* Системные функции:
		* Добавить в рантайм функции outln и errln [\#9](https://github.com/thewizardplusplus/micro/issues/9)
		* Добавить в рантайм функцию env [\#14](https://github.com/thewizardplusplus/micro/issues/14)
		* Добавить в рантайм функцию time [\#15](https://github.com/thewizardplusplus/micro/issues/15)
		* Поддерживать чтение строки в функции рантайма in [\#16](https://github.com/thewizardplusplus/micro/issues/16)
		* Добавить в рантайм функцию inln [\#39](https://github.com/thewizardplusplus/micro/issues/39)
		* Добавить поддержку вывода сообщения в функцию рантайма exit [\#45](https://github.com/thewizardplusplus/micro/issues/45)
* Обработка строк:
	* Упростить регулярные выражения символов и строк [\#23](https://github.com/thewizardplusplus/micro/issues/23)
	* Упростить функции quote и unquote [\#24](https://github.com/thewizardplusplus/micro/issues/24)
	* Добавить поддержку шестнадцатеричных escape-последовательностей [\#25](https://github.com/thewizardplusplus/micro/issues/25)
	* Удалять конечные нули из дробной части при преобразовании числа в строку [\#33](https://github.com/thewizardplusplus/micro/issues/33)
* Обработка ошибок:
	* Выбрасывать исключение при попытке преобразования в строку значения неизвестного типа [\#34](https://github.com/thewizardplusplus/micro/issues/34)
	* Выбрасывать исключение при попытке вычисления сущности неизвестного типа [\#35](https://github.com/thewizardplusplus/micro/issues/35)
	* Выбрасывать исключение при попытке создания функционального типа из неподходящего источника [\#40](https://github.com/thewizardplusplus/micro/issues/40)
	* Рефакторинг обработки ошибок [\#44](https://github.com/thewizardplusplus/micro/issues/44)
	* Добавить имя файла скрипта в сообщения об ошибках [\#48](https://github.com/thewizardplusplus/micro/issues/48)
	* Отображать исключения как все прочие ошибки [\#52](https://github.com/thewizardplusplus/micro/issues/52)
	* Определять позицию в коде и имя файла для ошибок времени выполнения [\#57](https://github.com/thewizardplusplus/micro/issues/57)
	* Обрабатывать исключение KeyboardInterrupt (<kbd>Ctrl+C</kbd>) [\#63](https://github.com/thewizardplusplus/micro/issues/63)
* Рефакторинг:
	* Удалить отладочный код [\#5](https://github.com/thewizardplusplus/micro/issues/5)
	* Привести стиль кода в соответствие с PEP 8 [\#6](https://github.com/thewizardplusplus/micro/issues/6)
	* Вынести тесты в примеры [\#11](https://github.com/thewizardplusplus/micro/issues/11)
	* Реорганизовать код [\#17](https://github.com/thewizardplusplus/micro/issues/17)
	* Рефакторинг встроенных функций [\#18](https://github.com/thewizardplusplus/micro/issues/18)
	* Рефакторинг препарсера [\#19](https://github.com/thewizardplusplus/micro/issues/19)
	* Вынести в отдельный класс преобразование в строку списка токенов [\#27](https://github.com/thewizardplusplus/micro/issues/27)
	* Рефакторинг парсера [\#41](https://github.com/thewizardplusplus/micro/issues/41)
	* Рефакторинг вспомогательных функций [\#42](https://github.com/thewizardplusplus/micro/issues/42)
	* Рефакторинг функционального типа [\#43](https://github.com/thewizardplusplus/micro/issues/43)
	* Вынести в отдельную функцию основной код [\#47](https://github.com/thewizardplusplus/micro/issues/47)
* pip-пакет:
	* Оформить pip-пакет [\#7](https://github.com/thewizardplusplus/micro/issues/7)
	* Подключить библиотеку PLY как зависимость pip-пакета [\#8](https://github.com/thewizardplusplus/micro/issues/8)
* Сниппеты:
	* Добавить в сниппеты пробелы в шаблонах с функциями [\#64](https://github.com/thewizardplusplus/micro/issues/64)
	* Добавить в сниппеты поддержку классов [\#65](https://github.com/thewizardplusplus/micro/issues/65)
	* Добавить в сниппеты заготовку для обхода списка [\#66](https://github.com/thewizardplusplus/micro/issues/66)
	* Добавить в сниппеты пробелы или переносы строк перед последним положением курсора [\#67](https://github.com/thewizardplusplus/micro/issues/67)
* Сделать скоуп замыканий независимым между их запусками [\#56](https://github.com/thewizardplusplus/micro/issues/56)
* Добавить возможности функции рантайма load по поиску файлов самому интерпретатору [\#55](https://github.com/thewizardplusplus/micro/issues/55)
* Добавить кеширование загружаемых скриптов [\#54](https://github.com/thewizardplusplus/micro/issues/54)
* Использовать независимые списки функций при парсинге и вычислениях [\#51](https://github.com/thewizardplusplus/micro/issues/51)
* Добавить новый пример &mdash; weasel program [\#50](https://github.com/thewizardplusplus/micro/issues/50)
* Изменить лицензию документации на CC BY 4.0 [\#28](https://github.com/thewizardplusplus/micro/issues/28)
* Игнорировать символ возврата каретки [\#26](https://github.com/thewizardplusplus/micro/issues/26)

## [v2.0](https://github.com/thewizardplusplus/micro/tree/v2.0) (2016-12-06)

* добавлена полустатическая типизация &mdash; статически типизированны только вызываемые типы (функции арности больше 0), остальные типы используют динамическую типизацию;
* благодаря появлению полустатической типизации:
	* парсинг кода осуществляется **до** его выполнения;
	* осуществляется построение AST;
* снято ограничение на глубину рекурсии (теперь рекурсия не ограничена ни Python, ни стеком);
* убраны:
	* автоматический вызов функций при их определении;
	* поддержка императивного программирования;
	* доступ к интерпретатору (функция `eval`);
* мутабельные структуры данных заменены на иммутабельные.

## [v1.0](https://github.com/thewizardplusplus/micro/tree/v1.0) (2016-02-15)

* Add docs:
    * Add the grammar description.
    * Add a brief of the lang description.
    * Add the lang description.
    * Add the runtime description.
    * Add the development plan.
* Make the set function immutable.
* Add command line arguments.
* Add an arity function.
* Correct a code requiring.

## [v0.23](https://github.com/thewizardplusplus/micro/tree/v0.23) (2016-02-13)

Add a plugin for the Atom editor.

## [v0.22](https://github.com/thewizardplusplus/micro/tree/v0.22) (2016-02-13)

* Add examples.
* Add a rand function.
* Extend a list access.
* Add a read function.

## [v0.21](https://github.com/thewizardplusplus/micro/tree/v0.21) (2016-02-12)

Add an options processing.

## [v0.20](https://github.com/thewizardplusplus/micro/tree/v0.20) (2016-02-12)

* Extend list functions.
* Extend math functions.
* Add an unary minus.
* Add an eval function.
* Add require functions.
* Add a type detection.
* Add an is_def function.
* Add an exit function.

## [v0.19](https://github.com/thewizardplusplus/micro/tree/v0.19) (2016-02-12)

Refactoring.

## [v0.18](https://github.com/thewizardplusplus/micro/tree/v0.18) (2016-02-07)

* Add a nil type.
* Add a support of an assignment to a parent scope.
* Add a while operator.
* Correct a result value for an empty token list.

## [v0.17](https://github.com/thewizardplusplus/micro/tree/v0.17) (2016-02-06)

Add a conditional operator.

## [v0.16](https://github.com/thewizardplusplus/micro/tree/v0.16) (2016-02-06)

* Add print functions.
* Add conversions.
* Add a creation of numbers as character tokens.
* Correct a string processing:
    * correct a parsing;
    * check that a string token is valid;
    * unescape string tokens.
* Correct the lexer: add punctuation restrictions.

## [v0.15](https://github.com/thewizardplusplus/micro/tree/v0.15) (2016-02-06)

* Add a support of float numbers.
* Add few new operations with numbers.
* Strengthen restrictions on operations with numbers.

## [v0.14](https://github.com/thewizardplusplus/micro/tree/v0.14) (2016-02-04)

Add a support of a boolean type.

## [v0.13](https://github.com/thewizardplusplus/micro/tree/v0.13) (2016-02-04)

Add a supports of lists and strings and replace the preprocession to the specially builtin function.

## [v0.12](https://github.com/thewizardplusplus/micro/tree/v0.12) (2016-02-03)

* Add an evaluation of an expression list into user functions.
* Allow a redeclaration of functions.
* Add a local function map.
* Add the preprocessor.

## [v0.11](https://github.com/thewizardplusplus/micro/tree/v0.11) (2016-02-03)

* Read a code from stdin.
* Add the lexer.
* Add a support of comments.

## [v0.10](https://github.com/thewizardplusplus/micro/tree/v0.10) (2016-02-02)

* Add an interpretation of an end of a token list as a creation of a closure.
* Add a support of closures for builtin functions.
* Remove a memorizing of anonymous functions.
* Add a printing of a function body.

## [v0.9](https://github.com/thewizardplusplus/micro/tree/v0.9) (2016-02-01)

Add an evaluation of an expression list.

## [v0.8](https://github.com/thewizardplusplus/micro/tree/v0.8) (2016-01-31)

Add an using of outer arguments into user functions.

## [v0.7](https://github.com/thewizardplusplus/micro/tree/v0.7) (2016-01-31)

Add an applying of closures as result values.

## [v0.6](https://github.com/thewizardplusplus/micro/tree/v0.6) (2016-01-31)

Add an applying of closures as function arguments.

## [v0.5](https://github.com/thewizardplusplus/micro/tree/v0.5) (2016-01-31)

Add a creation of closures (with a parameters binding).

## [v0.4](https://github.com/thewizardplusplus/micro/tree/v0.4) (2016-01-31)

Add an using of arguments into user functions.

## [v0.3](https://github.com/thewizardplusplus/micro/tree/v0.3) (2016-01-31)

Add an evaluation of user functions.

## [v0.2](https://github.com/thewizardplusplus/micro/tree/v0.2) (2016-01-23)

Add a parsing of user functions.

## [v0.1](https://github.com/thewizardplusplus/micro/tree/v0.1) (2016-01-20)

Add a basic evaluation: functions &mdash; only built-in (supports: `+`, `-`, `*`, `/`), values &mdash; only natural numbers.

Lexer not implemented &mdash; requires to input a list of tokens.

*This change log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator).*