#!/usr/bin/env python3
from lib import *
import curses


window = curses.initscr()
curses.noecho()
window2 = curses.newwin(40, 10, 10, 10)

test_printable = Printable(
    True,
    window,
    0,
    {"?", "?", "."},
    200,
    40,
    True,
    Newline_None,
    "textxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)

test_printable.slow_print()
test_printable.window = window2
test_printable.slow_print()
curses.endwin()
