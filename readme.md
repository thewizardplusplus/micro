# Micro

## Usage

```
$ python3 micro -v | --version
$ python3 micro -h | --help
$ python3 micro [-t TARGET | --target TARGET] [<script>] [<args>...]
```

Options:

* `-v`, `--version` &mdash; show the version message and exit;
* `-h`, `--help` &mdash; show the help message and exit;
* `-t TARGET`, `--target TARGET` &mdash; set a target of a script processing; it can take following values:
	* `tokens`;
	* `preast`;
	* `ast`;
	* `evaluation` (it's a default value).

Arguments:

* `<script>` &mdash; a script (if it's empty or equals to `-`, then it'll read a script from stdin; a default value: `-`);
* `<args>` &mdash; script arguments.

## IDE support

* [Atom](http://atom.io/) plugin: [language-micro](tools/atom-plugin/language-micro).

## Docs

* [Brief](docs/brief.md) (ru).
* [Description](docs/description.md) (ru).
* [Grammar](docs/grammar.md).
* [Runtime](docs/runtime.md) (ru).

## License

The MIT License (MIT)

Copyright &copy; 2016, 2017 thewizardplusplus <thewizardplusplus@yandex.ru>
