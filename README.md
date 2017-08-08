# Micro

Interpreter of the Micro programming language.

## Installation

Clone this repository:

```
$ git clone https://github.com/thewizardplusplus/micro.git
$ cd micro
```

Then install the interpreter with [pip](https://pip.pypa.io/) tool:

```
$ sudo -H python3.5 -m pip install .
```

`sudo` command is required to install `micro` console script. If it's not required, `sudo` command can be omitted:

```
$ python3.5 -m pip install .
```

But then the interpreter should be started as `python3.5 -m micro`.

### Fix the warning from PLY library

When you're running the interpreter, you can get the following error:

```
WARNING: Couldn't create 'parsetab'. [Errno 13] Permission denied: '/usr/local/lib/python3.5/dist-packages/micro/parsetab.py'
```

In this case, you need to adjust permissions of the specified file:

```
$ sudo touch /usr/local/lib/python3.5/dist-packages/micro/parsetab.py
$ sudo chown "$USER:$USER" /usr/local/lib/python3.5/dist-packages/micro/parsetab.py
```

## Usage

```
$ micro -v | --version
$ micro -h | --help
$ micro [-t TARGET | --target TARGET] [<script>] [<args>...]
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
* [Library](docs/library.md) (ru).

## License

The MIT License (MIT)

Copyright &copy; 2016, 2017 thewizardplusplus
