Getting Started
===============

Installation
------------

Just install CharPrint via pip:

.. code-block:: console

    pip install charprint

Note that the Windows version will require windows-curses wheels. They should be installed automatically, but if they don't for some reason you can do so with

.. code-block:: console

    pip install windows-curses


Quickstart
----------
.. code-block:: python

    window1 = initscr()
    window2 = newwin(10, 10, 5, 5)

    window_one_printable = Printable(text="This is some example text".)
