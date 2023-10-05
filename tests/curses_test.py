#!/usr/bin/env python3
import pytest
from .lib import *


def test_initialization():
    test_curses_window1 = curses.initscr()
    test_curses_printable = Printable(
        True,
        test_curses_window1,
        40,
        {".", "?", "!"},
        200,
        40,
        False,
        Newline_None,
        "This is test text",
    )
    return test_curses_window1, test_curses_printable


test_curses_window, test_curses_printable = test_initialization()
print(test_curses_printable)
