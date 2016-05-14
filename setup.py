from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    README = f.read()
with open(path.join(here, 'CHANGES.txt'), encoding='utf-8') as f:
    CHANGES = f.read()


setup(
    name='pyramid_ptpython',
    version="1.1.1",

    description='A ptpython and ptipython plugin for pyramid pshell',
    long_description=README + '\n\n' + CHANGES,

    packages=find_packages(),
    exclude_package_data={'': ['.gitignore']},
    zip_safe=True,

    author='Daniel Kraus',
    author_email='dakra-python@tr0ll.net',
    url='https://github.com/dakra/pyramid_ptpython',
    license='ISC',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: Pyramid',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='pyramid pshell ptpython',

    setup_requires=['setuptools_git'],
    install_requires=[
        'pyramid > 1.6a2',
        'ptpython',
    ],
    py_modules=['pyramid_ptpython'],
    extras_require={'ipython': ['ipython']},
    entry_points={
        'pyramid.pshell_runner': [
            'ptpython = pyramid_ptpython:ptpython_shell_runner',
            'ptipython = pyramid_ptpython:ptipython_shell_runner',
        ]
    }
)
