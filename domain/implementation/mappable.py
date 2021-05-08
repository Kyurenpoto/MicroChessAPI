# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from typing import Callable, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class Mappable(Generic[T]):
    __slots__ = ["__value"]

    __value: T

    def __init__(self, target: T):
        self.__value = target

    def value(self) -> T:
        return self.__value

    def mapped(self, mapper: Callable[[T], U]) -> Mappable[U]:
        return Mappable[U](mapper(self.__value))
