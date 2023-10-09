#!/usr/bin/env python3

from dataclasses import dataclass, field


@dataclass
class NewlineStatus(type):
    _instances: dict = field(default_factory=dict)

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(NewlineStatus, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass
class NewlineStart(NewlineStatus):
    pass


@dataclass
class NewlineEnd(NewlineStatus):
    pass


@dataclass
class NewlineNone(NewlineStatus):
    pass


@dataclass
class NewlineBoth(NewlineStatus):
    pass


@dataclass
class StreamSetting:
    pass


@dataclass
class ListOut(StreamSetting):
    pass


@dataclass
class WrappedListOut(StreamSetting):
    pass


@dataclass
class GenOut(StreamSetting):
    pass


@dataclass
class WordListOut(StreamSetting):
    pass


@dataclass
class WordGenOut(StreamSetting):
    pass


@dataclass
class WrappedGenOut(StreamSetting):
    pass
