# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations
from typing import Optional, TypeVar, Generic, Callable

T = TypeVar('T')
U = TypeVar('U')

class Nullable(Generic[T]):
    __slots__ = ["__value"]

    __value: Optional[T]

    def __init__(self, target: Optional[T]):
        self.__value = target

    def value(self) -> Optional[T]:
        return self.__value

    def op(self, func: Callable[[Optional[T]], Optional[U]]) -> Nullable[U]:
        return Nullable[U](
            None if self.__value is None else func(self.__value))
