# CharPrint

CharPrint is a simple but flexible library intended for expressive text, such as digital poetry and text-based games. It can be used with curses windows, a bare console, or to output characters that can be incorporated into your pipeline.

**Note:** Currently in active development.

## Concepts
The core of CharPrint is the Printable class. This is an object that represents some text, a collection of associated settings, and, optionally, an associated curses window. The Printable can be manipulated, have its settings changed, and print character by character with various ways of changing the pacing. This allows a highly object-oriented, simple, and flexible approach to text for creative projects. The text of a Printable can also be surfaced as a list or generator, allowing you to incorporate them into external pipelines.

## API Reference

[Read the docs online](https://charprint.readthedocs.io/en/latest/) or the local copy at docs/build/html/index.html.

