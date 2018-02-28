import setuptools
import re
import sys
import os.path
import glob

if not (0x030500f0 <= sys.hexversion < 0x040000a0):
    raise Exception('requires Python >=3.5, <4.0')

project_path = os.path.dirname(os.path.abspath(__file__))
package_name, *_ = setuptools.find_packages()
package_path = os.path.join(project_path, package_name)
with open(
    os.path.join(package_path, 'utilities.py'),
    encoding='utf-8',
) as utilities_file:
    version = re.search(
        r"^MICRO_VERSION = '([^']+)'$",
        utilities_file.read(),
        re.MULTILINE,
    ).group(1)

with open(
    os.path.join(project_path, 'README.md'),
    encoding='utf-8',
) as readme_file:
    long_description = readme_file.read()
long_description = long_description[
    long_description.find('## Installation')
    : long_description.find('## IDE support')
].rstrip()
try:
    import pypandoc

    long_description = pypandoc.convert_text(long_description, 'rst', 'md')
except ImportError:
    pass

setuptools.setup(
    name=package_name,
    version=version,
    description='Interpreter of the Micro programming language',
    long_description=long_description,
    license='MIT',
    author='thewizardplusplus',
    author_email='thewizardplusplus@yandex.ru',
    url='https://github.com/thewizardplusplus/' + package_name,
    packages=[
        package_name,
    ],
    package_data={
        package_name: glob.glob(
            os.path.join(package_path, 'data/**/*.micro'),
            recursive=True,
        ),
    },
    install_requires=[
        'ply >=3.10, <4.0',
        'python-dotenv >=0.7.1, <1.0',
    ],
    python_requires='>=3.5, <4.0',
    entry_points={
        'console_scripts': [
            '{0} = {0}:main'.format(package_name),
        ],
    },
)
