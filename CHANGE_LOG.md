# Change Log

## [v2.2](https://github.com/thewizardplusplus/micro/tree/v2.2) (2018-01-11)

* Перевести имена служебных файлов в верхний регистр [\#97](https://github.com/thewizardplusplus/micro/issues/97)
* Возвращать код завершения 1 при перехвате исключения KeyboardInterrupt \(Ctrl+C\) [\#101](https://github.com/thewizardplusplus/micro/issues/101)
* Добавить поддержку shebang [\#102](https://github.com/thewizardplusplus/micro/issues/102)
* Привести к единообразию обработку концов строк [\#116](https://github.com/thewizardplusplus/micro/issues/116)
* Вернуть поддержку многострочных строковых литералов [\#132](https://github.com/thewizardplusplus/micro/issues/132)
* Потенциальная поддержка REPL:
	* Скорректировать обработку исключений во время вычислений [\#78](https://github.com/thewizardplusplus/micro/issues/78)
	* Поддерживать повторные вычисления с тем же списком функций [\#79](https://github.com/thewizardplusplus/micro/issues/79)
	* Добавить заглушки для генерируемых функций рантайма [\#109](https://github.com/thewizardplusplus/micro/issues/109)
	* Хранить ошибки индивидуально в каждом экземпляре парсера [\#110](https://github.com/thewizardplusplus/micro/issues/110)
* Рефакторинг:
	* Выделить отдельную функцию для парсинга кода из строки [\#108](https://github.com/thewizardplusplus/micro/issues/108)
	* Выделить отдельную функцию для выполнения кода из строки [\#118](https://github.com/thewizardplusplus/micro/issues/118)
	* Выделить логику выбора конкретного файла для загрузки в отдельный подпакет [\#126](https://github.com/thewizardplusplus/micro/issues/126)
	* Выделить логику кеширования загружаемых файлов в отдельный класс [\#127](https://github.com/thewizardplusplus/micro/issues/127)
* Рантайм:
	* Удалить функцию рантайма arity [\#85](https://github.com/thewizardplusplus/micro/issues/85)
	* Добавление функций:
		* Добавить в рантайм функцию bool [\#70](https://github.com/thewizardplusplus/micro/issues/70)
		* Добавить в рантайм поддержку NaN и infinity [\#92](https://github.com/thewizardplusplus/micro/issues/92)
		* Добавить в рантайм константы pi и e [\#93](https://github.com/thewizardplusplus/micro/issues/93)
		* Добавить в рантайм функцию sleep [\#106](https://github.com/thewizardplusplus/micro/issues/106)
		* Добавить в рантайм функцию seed [\#112](https://github.com/thewizardplusplus/micro/issues/112)
		* Добавить в рантайм функцию is\_main [\#129](https://github.com/thewizardplusplus/micro/issues/129)
	* Изменение функций:
		* Добавить функции рантайма env поддержку конфигов .env [\#72](https://github.com/thewizardplusplus/micro/issues/72)
		* Поменять порядок аргументов в функции рантайма angle [\#134](https://github.com/thewizardplusplus/micro/issues/134)
		* Функция load:
			* Поддерживать задание внешней реализации функции рантайма load [\#103](https://github.com/thewizardplusplus/micro/issues/103)
			* Обернуть функцию рантайма load в closure\_trampoline [\#130](https://github.com/thewizardplusplus/micro/issues/130)
* Библиотека:
	* Дополнить библиотеку для работы со списками [\#98](https://github.com/thewizardplusplus/micro/issues/98)
	* Поиск файлов при загрузке:
		* Включить библиотеку в pip-пакет [\#73](https://github.com/thewizardplusplus/micro/issues/73)
		* Добавить место установки pip-пакета как путь для поиска скриптов после переменной MICRO\_LIBRARY [\#74](https://github.com/thewizardplusplus/micro/issues/74)
		* Поддерживать указание нескольких путей в переменной MICRO\_LIBRARY [\#77](https://github.com/thewizardplusplus/micro/issues/77)
	* Изменение функций:
		* Упростить функцию библиотеки ansi [\#89](https://github.com/thewizardplusplus/micro/issues/89)
		* Доработать функцию библиотеки generate [\#111](https://github.com/thewizardplusplus/micro/issues/111)
		* Поменять порядок аргументов в функции библиотеки reduce [\#135](https://github.com/thewizardplusplus/micro/issues/135)
	* Удаление функций:
		* Удалить функцию библиотеки count [\#105](https://github.com/thewizardplusplus/micro/issues/105)
		* Удалить из библиотеки модуль для юнит-тестирования [\#107](https://github.com/thewizardplusplus/micro/issues/107)
* Примеры:
	* Удалить из примеров тесты [\#83](https://github.com/thewizardplusplus/micro/issues/83)
	* Улучшить стиль кода в примерах [\#133](https://github.com/thewizardplusplus/micro/issues/133)
	* Выделить общий код из примеров [\#138](https://github.com/thewizardplusplus/micro/issues/138)
	* Добавление примеров:
		* Добавить новый пример - перцептрон [\#120](https://github.com/thewizardplusplus/micro/issues/120)
		* Добавить новый пример - множество Мандельброта [\#121](https://github.com/thewizardplusplus/micro/issues/121)
		* Добавить новый пример - сфера [\#124](https://github.com/thewizardplusplus/micro/issues/124)
		* Добавить новый пример - 2D-жизнь [\#125](https://github.com/thewizardplusplus/micro/issues/125)
	* Пример 1D-жизнь:
		* Убрать закольцовывание из примера 1D-жизнь [\#131](https://github.com/thewizardplusplus/micro/issues/131)
		* Разделить пример 1D-жизни на модули [\#137](https://github.com/thewizardplusplus/micro/issues/137)
		* Вынести магические константы из примера 1D-жизнь в его параметры [\#139](https://github.com/thewizardplusplus/micro/issues/139)
* pip-пакет:
	* Указать в setup.py требуемую версию Python [\#75](https://github.com/thewizardplusplus/micro/issues/75)
	* Рефакторинг парсинга версии pip-пакета [\#100](https://github.com/thewizardplusplus/micro/issues/100)
	* Убрать явную установку группы для файла parsetab.py [\#119](https://github.com/thewizardplusplus/micro/issues/119)
* Плагин для редактора Atom:
	* Удалить поддержку сниппетов из плагина для редактора Atom [\#80](https://github.com/thewizardplusplus/micro/issues/80)
	* Упростить обработку отступов в плагине для редактора Atom [\#81](https://github.com/thewizardplusplus/micro/issues/81)
	* Добавить описание установки в плагин для редактора Atom [\#82](https://github.com/thewizardplusplus/micro/issues/82)
	* Улучшить стиль кода в плагине для редактора Atom [\#86](https://github.com/thewizardplusplus/micro/issues/86)
* Документация:
	* Упростить регулярные выражения для пунктуационных идентификаторов в документации [\#87](https://github.com/thewizardplusplus/micro/issues/87)
	* Изменить в документации описание типизации со слабой на сильную [\#99](https://github.com/thewizardplusplus/micro/issues/99)
	* Исправить описание некоторых функций рантайма в документации [\#117](https://github.com/thewizardplusplus/micro/issues/117)
	* Общее описание:
		* Дополнить описание модульности в документации [\#123](https://github.com/thewizardplusplus/micro/issues/123)
		* Дополнить описание требований к файлам исходного кода в документации [\#136](https://github.com/thewizardplusplus/micro/issues/136)
	* Библиотека:
		* Указать наименование \(путь\) модулей в документации на библиотеку [\#104](https://github.com/thewizardplusplus/micro/issues/104)
		* Поменять порядок функций в документации на библиотеку [\#122](https://github.com/thewizardplusplus/micro/issues/122)
	* Оформление:
		* Добавить логотип языка [\#90](https://github.com/thewizardplusplus/micro/issues/90)
		* Добавить оглавление к документации [\#96](https://github.com/thewizardplusplus/micro/issues/96)
		* Исправить знак копирайта [\#140](https://github.com/thewizardplusplus/micro/issues/140)

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
