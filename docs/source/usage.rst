Usage
=========================

charprint
---------
.. py:module:: charprint

               The primary module of the library.

.. py:class:: Printable(curses_enabled: bool = False, window=None, text_speed: int = 40, pause_at: set = {".", "?", "!"}, pause_delay: int = 200, wrap_point: int = 40, wait_at_end: bool = False, newline_option: Type[NewlineStatus] = NewlineNone, text: str = "")

              .. py:attribute:: curses_enabled: bool = False

                                If True, prints to a curses window instead of the bare console.

              .. py:attribute:: window = None

                              If curses is enabled, this is the curses window this printable will print to. Otherwise is ignored.

              .. py:attribute:: text_speed: int = 40

                                The amount of time in milliseconds to wait between each character when printing.

              .. py:attribute:: pause_at: set = {".", "?", "!"}

                                Specific characters to pause for a longer (or shorter) time than the default text_speed. As this is a set, you don't have to worry about cluttering it by accidentally adding multiples of the same character.

              .. py:attribute:: pause_delay: int = 200

                                The amount of time in milliseconds to wait at the characters in the pause_at set.

              .. py:attribute:: wrap_point: int = 40

                                The amount of characters after which the printer will wrap the text to the next line, givin you more formatting control and preventing words being split.

              .. py:attribute:: wait_at_end: bool = False

                                If True, the program will wait for the user to press a key once the printing is complete.

              .. py:attribute:: newline_option: Type[NewlineStatus] = NewlineNone

                                A custom type with options NewlineNone, NewlineStart, NewlineEnd, or NewlineBoth (subclassing NewlineStatus). Adds a newline to the print at the beginning, end, both or nowhere.

              .. py:attribute:: text: str = ""

                                The text that is printed by the printable instance.



    .. py:method:: char_print(text = None)

    Prints text to the curses window or console depending on curses_enabled. If text is given in the function argument it prints that text, otherwise it prints the given printable's text field.

    The text is printed character by character, with text_speed delay (in ms) between each. The printer will pause for pause_at delay at any character in the pause_at set, if any. While printing, the text will be wrapped at wrap_point number of characters. If wait_at_end is True, after the text is printed the program will wait for the user to press a key before continuing. newline_option optionally adds a newline to the beginning or end or both of the printed text.

    :param text: Option to print text passed in the function instead of the printable's text field.
    :type text: str or None.

    .. py:method:: clear

                   Either clears the console or clears the Printable's curses window.


    .. py:method:: stream_out(stream_setting: Type[StreamSetting])

    Stream out a printable's text field, for use in your own systems. Possible stream_settings:

    :param stream_setting: How to return self.text.
    :type stream_setting: GenOut, WrappedGenOut, WordGenOut, ListOut, WordListOut, or WrappedListOut
    :return: A generator or list grouped by character, word, or wrap point.
    :rtype: list[str] or generator(str)

support functions
-----------------

Various functions outside the class that provide additional functionality.

.. py:function:: charprint.clear_all_windows(windows: tuple[curses.window], refresh: bool = True):

                 Clears a tuple of curses windows.

                 :param windows: Tuple of curses windows to clear.
                 :type windows: tuple[curses.window]
                 :param refresh: If False, the windows will not automatically refresh. You must refresh the windows to see the change.
                 :type refresh: bool

.. py:function:: charprint.refresh_all_windows(windows: tuple):

                 Refreshes a tuple of curses windows.

                 :param windows: Tuple of curses windows to refresh.
                 :type windows: tuple



charprint_types
---------------
.. py:module:: charprint_types

               The module containing custom types used for toggling various options.

.. py:class:: NewlineStatus

              Superclass that defines the "type" used to set NewlineStatus for a Printable.

              .. py:attribute:: Subtypes

                                NewlineEnd, NewlineStart, NewlineBoth, NewlineNone

.. py:class:: StreamSetting

              Superclass that defines the "type" used to set the return type for the stream out funciton.

              .. py:attribute:: Subtypes

                                ListOut, WrappedListOut, WordListOut, GenOut, WordGenOut, WrappedGenOut
