#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import Type
import pytest
from time import sleep
from textwrap import fill, wrap
import console
from console import utils as conutils
import importlib
from charprint_types import (
    NewlineEnd,
    NewlineStart,
    NewlineNone,
    NewlineBoth,
    NewlineStatus,
    StreamSetting,
    ListOut,
    WrappedListOut,
    GenOut,
    WordListOut,
    WordGenOut,
    WrappedGenOut,
)
from unicurses import *

# TODO: Add a function that just outputs a string


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
        newline_option: Type[NewlineStatus] = NewlineNone,
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
                    f"{new_status} is not a valid Newline Status. Try NewlineStart, NewlineEnd, NewlineBoth, or NewlineNone"
                )
        except:
            raise TypeError(
                f"{new_status} is not a valid Newline Status. Try NewlineStart, NewlineEnd, NewlineBoth, or NewlineNone"
            )

    @property
    def window(self):
        return self._window

    @window.setter
    def window(self, new_window):
        try:
            self._window = new_window
        except:
            raise TypeError("Window must be a curses window or None.")

    def char_print(self, text=None):
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
        if self._newline is NewlineStart or self._newline is NewlineBoth:
            self._window.addch("\n")

        for c in fill(text_to_print, self.wrap_point):
            self._window.addch(c)
            self._window.refresh()
            if c in self.pause_at:
                sleep(self.pause_delay / 1000)
            else:
                sleep(self.text_speed / 1000)

        if self._newline is NewlineEnd or self._newline is NewlineBoth:
            self._window.addch("\n")

        if self.wait_at_end is True:
            self._window.timeout(-1)
            self._window.getch()

    def __console_print(self, text_to_print):
        if self._newline is NewlineStart or self._newline is NewlineBoth:
            print("\n")

        for c in fill(text_to_print, self.wrap_point):
            print(c, end="")
            if c in self.pause_at:
                sleep(self.pause_delay / 1000)
            else:
                sleep(self.text_speed / 1000)

        if self._newline is NewlineEnd or self._newline is NewlineBoth:
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

    def stream_out(self, stream_setting: Type[StreamSetting]):
        """Produces a Printable's text property as a list of characters, wrapped characters, words, or as a generator that yields a series of individual characters, wrapped characters, or words allowing it to be used as input in your own systems."""
        if stream_setting is ListOut:
            return list(self.text)
        elif stream_setting is WrappedListOut:
            return wrap(self.text, self.wrap_point)
        elif stream_setting is WordListOut:
            return self.text.split()
        elif stream_setting is GenOut:
            return (c for c in self.text)
        elif stream_setting is WordGenOut:
            return (c for c in self.text.split())
        elif stream_setting is WrappedGenOut:
            return (c for c in wrap(self.text, self.wrap_point))
        else:
            raise TypeError("Invalid stream setting!")


def clear_all_windows(windows: tuple, refresh: bool = True):
    """Clears all curses windows in the given tuple. If refresh is True, immediately refreshes all the passed windows."""
    for element in windows:
        element.erase()
    if refresh is True:
        refresh_all_windows(windows)


def refresh_all_windows(windows: tuple):
    """Refreshes all the curses windows in a tuple of windows."""
    for element in windows:
        element.refresh()
