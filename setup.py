try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = { \
	'name': 'micro', \
	'description': 'The interpreter of the programming language Micro.', \
	'version': '0.19', \
	'url': 'https://github.com/thewizardplusplus/micro', \
	'download_url': 'https://github.com/thewizardplusplus/micro', \
	'author': 'thewizardplusplus', \
	'author_email': 'thewizardplusplus@yandex.ru', \
	'packages': ['micro'], \
	'install_requires': [], \
	'scripts': [] \
}

setup(**config)
