# CharPrint

CharPrint is a simple but flexible library intended for expressive text, such as digital poetry and text-based games. It can be used with curses windows, a bare console, or to output characters that can be incorporated into your pipeline.

**Note:** Currently in active development.

## Concept
The core of CharPrint is the Printable class. This is an object that represents some text, a collection of associated settings, and, optionally, an associated curses window. The Printable can be manipulated, have its settings changed, and print character by character with various ways of changing the pacing. This allows a highly object-oriented, simple, and flexible approach to text for creative projects. The text of a Printable can also be surfaced as a list or generator, allowing you to incorporate them into external pipelines.

## Details and API Reference

[Read the docs online](https://charprint.readthedocs.io/en/latest/) or the local copy at docs/build/html/index.html.

## Quickstart

``` shell
# Install with pip
pip install charprint
```


``` python
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
```
