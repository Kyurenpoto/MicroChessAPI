# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from .basictype import SAN


class MicroSAN:
    __slots__ = ["__index", "__sans", "__san"]

    __index: int
    __sans: list[str]
    __san: SAN

    def __init__(self, index: int, sans: list[str]):
        self.__index = index
        self.__sans = sans
        self.__san = SAN("")

    def san(self) -> SAN:
        if self.__san == SAN(""):
            self.__san = SAN(self.__sans[self.__index])

        return self.__san

    def index(self) -> int:
        return self.__index

    def sans(self) -> list[str]:
        return self.__sans
