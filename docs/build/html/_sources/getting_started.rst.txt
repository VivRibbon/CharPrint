Getting Started
===============

Installation
------------

Just install CharPrint via pip:

.. code-block:: console

    pip install charprint

Note that unicurses is a dependency, which should allow the library to work on Windows. It should be installed as a dependency, but if not you can install it with

.. code-block:: console

    pip install uni-curses


Quickstart
----------
.. code-block:: python

    # Printing to the console

    # Instantiate a printable object
    console_printable = Printable(text_speed=20, pause_at: {".", ":", ";"}, text="This text will go to the console.")

    # Print the printable
    console_printable.char_print()

    # Change some settings
    console_printable.newline = NewlineBoth
    console_printable.wait_at_end = True

    # Print again, this time with text passed to the printing function
    console_printable.slow_print("The printable's text field is preserved, but this text is printed instead.")

    # Clear the console
    console_printable.clear()

    # Printing with curses

    # Initialize some windows (see the Python curses module documentation for details on general curses functionality.)
    window1 = initscr()
    window2 = newwin(10, 10, 5, 5)

    # Instantiate printables with the created windows
    window_one_printable = Printable(curses_enabled=True, window=window1, text="This is some example text".)
    window_two_printable = Printable(curses_enabled=True, window=window2, pause_delay: 400, wrap_point: 5, wait_at_end: True)

    # Print each printable's text to its assigned window
    window_one_printable.char_print()
    window_two_printable.char_print()

    # Create a new curses window and move the first printable to it
    window3 = newwin(20, 5, 10, 10)
    window_one_printable.window = window3
    window_one_printable.slow_print("Passing text into the function works in curses too, of course.")

    # Clear all three windows
    clear_all_windows((window1, window2, window3))

    # Stream a printable's text out for use in an external function

    # Produce a list from the printable's characters
    window_one_printable.stream_out(ListOut)

    # Produce a list of characters grouped by the wrap point
    window_two_printable.stream_out(WrappedListOut)

    # Produce a generator that yields each word of the printable
    window_one_printable.stream_out(WordGenOut)
