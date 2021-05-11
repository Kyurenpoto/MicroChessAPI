# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod

from .basictype import SAN


class Square(metaclass=ABCMeta):
    @abstractmethod
    def value(self) -> str:
        pass

    def file(self) -> str:
        return self.value()[0]

    def rank(self) -> str:
        return self.value()[1]


class FromSquare(Square):
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> str:
        return self.__san[:2]


class ToSquare(Square):
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> str:
        return self.__san[2:4]
