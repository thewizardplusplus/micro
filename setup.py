import setuptools
import re
import sys
import os.path
import glob

if not (0x030500f0 <= sys.hexversion < 0x040000a0):
    raise Exception('requires Python >=3.5, <4.0')

package_name, *_ = setuptools.find_packages()
package_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    package_name,
)
with open(
    os.path.join(package_path, 'utilities.py'),
    encoding='utf-8',
) as utilities_file:
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
    ],
    python_requires='>=3.5, <4.0',
    entry_points={
        'console_scripts': [
            '{0} = {0}:main'.format(package_name),
        ],
    },
)
