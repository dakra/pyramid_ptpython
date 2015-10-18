pyramid_ptpython
================

A `ptpython <https://github.com/jonathanslenders/ptpython/>`_ and ``ptipython`` plugin
for `pyramid <http://www.pylonsproject.org/>`_ pshell.


Installation
------------

Install from PyPI using ``pip`` or ``easy_install``.

.. code-block:: bash

    $ pip install pyramid_ptpython


You can also add the ``ipython`` dependency for ``ptipython``:

.. code-block:: bash

    $ pip install pyramid_ptpython[ipython]


Usage
-----

Simply pass ``ptpython`` or ``ptipython`` as shell argument to pyramids ``pshell``.

.. code-block::

    $ pshell -p ptpython development.ini
