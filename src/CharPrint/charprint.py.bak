#!/usr/bin/env python3

import curses
from dataclasses import dataclass, field
from typing import Type
import pytest
from time import sleep
from textwrap import fill
import console
from console import utils as conutils


@dataclass
class NewlineStatus(type):
    _instances: dict = field(default_factory=dict)

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(NewlineStatus, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass
class Newline_Start(NewlineStatus):
    pass


@dataclass
class Newline_End(NewlineStatus):
    pass


@dataclass
class Newline_None(NewlineStatus):
    pass


@dataclass
class Newline_Both(NewlineStatus):
    pass


class Printable:
    """The core object of char_print - represents a chunk of text and associated display info."""

    def __init__(
        self,
        curses_enabled: bool = False,
        window=None,
        text_speed: int = 40,
        pause_at: set = {".", "?", "!"},
        pause_delay: int = 200,
        wrap_point: int = 40,
        wait_at_end: bool = False,
        newline_option: Type[NewlineStatus] = Newline_None,
        text: str = "",
    ):
        """Init"""
        self._newline = newline_option
        self.curses_enabled = curses_enabled
        self._window = window
        self.text = text
        self.text_speed = text_speed
        self.pause_at = pause_at
        self.pause_delay = pause_delay
        self.wrap_point = wrap_point
        self.wait_at_end = wait_at_end

    def __str__(self):
        return f"""Curses Enabled: {self.curses_enabled}
Window: {self._window}
Text Speed: {self.text_speed} ms
Pause At: {self.pause_at}
Pause Delay: {self.pause_delay} ms
Wrap Point: {self.wrap_point} characters
Wait At End: {self.wait_at_end}
{self._newline}
Text: {self.text[0:40]}{f" ... {self.text[len(self.text) - 20: len(self.text) + 1]}" if len(self.text) > 65 else ""}"""

    def __repr__(self):
        return f"""Printable(curses={self.curses_enabled}, window={self._window}, text_speed={self.text_speed}, pause_at={self.pause_at}, pause_delay={self.pause_delay}, wrap_point={self.wrap_point}, wait_at_end={self.wait_at_end}, newline_option={repr(self.newline)}, text={repr(self.text)})"""

    @property
    def newline(self):
        return self._newline

    @newline.setter
    def newline(self, new_status: Type[NewlineStatus]):
        try:
            if issubclass(new_status, NewlineStatus):
                self._newline = new_status
            else:
                raise TypeError(
                    f"{new_status} is not a valid Newline Status. Try Newline_Start, Newline_End, Newline_Both, or Newline_None"
                )
        except:
            raise TypeError(
                f"{new_status} is not a valid Newline Status. Try Newline_Start, Newline_End, Newline_Both, or Newline_None"
            )

    @property
    def window(self):
        return self._window

    @window.setter
    def window(self, new_window):
        if isinstance(new_window, curses.window) or new_window is None:
            self._window = new_window
        else:
            raise TypeError("Window must be a curses window or None.")

    def slow_print(self, text=None):
        """Print dispatcher. Checks if there is anything in the text argument and sends either that or self.text to a print function depending on whether curses is enabled for that Printable."""
        if text != None:
            text_to_print = text
        else:
            text_to_print = self.text
        match self.curses_enabled:
            case True:
                self.__curses_print(text_to_print)
            case False:
                self.__console_print(text_to_print)

    def __curses_print(self, text_to_print):
        if self._window == None:
            raise TypeError("No curses window attached to this printable! ")
        if self._newline is Newline_Start or self._newline is Newline_Both:
            self._window.addch("\n")

        for c in fill(text_to_print, self.wrap_point):
            self._window.addch(c)
            self._window.refresh()
            if c in self.pause_at:
                sleep(self.pause_delay / 1000)
            else:
                sleep(self.text_speed / 1000)

        if self._newline is Newline_End or self._newline is Newline_Both:
            self._window.addch("\n")

        if self.wait_at_end is True:
            self._window.timeout(-1)
            self._window.getch()

    def __console_print(self, text_to_print):
        if self._newline is Newline_Start or self._newline is Newline_Both:
            print("\n")

        for c in fill(text_to_print, self.wrap_point):
            print(c, end="")
            if c in self.pause_at:
                sleep(self.pause_delay / 1000)
            else:
                sleep(self.text_speed / 1000)

        if self._newline is Newline_End or self._newline is Newline_Both:
            print("\n")

        if self.wait_at_end:
            conutils.pause("")

    def clear(self):
        """Clear function fronted to the user. Calls either curses clear or console clear depnding on whether or not curses is enabled on the given printable."""
        match self.curses_enabled:
            case True:
                self.__curses_clear()
            case False:
                self.__console_clear()

    def __curses_clear(self):
        """Clears the given curses window. The user is meant to use clear() as a frontend for this function."""
        self._window.erase()
        self._window.refresh()

    def __console_clear(self):
        """Clears the console. The user is meant to use clear() as a frontend for this function."""
        conutils.cls()


def clear_all_windows(windows: tuple[curses.window], refresh: bool = True):
    """Clears all curses windows in the given tuple. If refresh is True, immediately refreshes all the passed windows."""
    for element in windows:
        element.erase()
        if refresh is True:
            element.refresh()


def refresh_all_windows(windows: tuple):
    """Refreshes all the curses windows in a tuple of windows."""
    for element in windows:
        element.refresh()
