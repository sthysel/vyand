from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup, find_packages

setup(
    name='vyand',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'vyand=vyand.cli:cli',
        ]
    },
    install_requires=[
        'click',
        'arrow',
        'pyserial',
        'scapy-python3',
        'tabulate',
        'attentive',
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
)
