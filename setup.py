import setuptools
import re

package_name, *_ = setuptools.find_packages()
with open('{}/utilities.py'.format(package_name), 'r') as utilities_file:
    version = re.search(
        r"^MICRO_VERSION = '([^']+)'$",
        utilities_file.read(),
        re.MULTILINE,
    ).group(1)
setuptools.setup(
    name=package_name,
    version=version,
    license='MIT',
    author='thewizardplusplus',
    author_email='thewizardplusplus@yandex.ru',
    url='https://github.com/thewizardplusplus/{}'.format(package_name),
    packages=[
        package_name,
    ],
    install_requires=[
        'ply >=3.10, <4.0',
    ],
    entry_points={
        'console_scripts': [
            '{0} = {0}:main'.format(package_name),
        ],
    },
)
