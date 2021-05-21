# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final

MSG_INVALID_LENGTH: Final[str] = "The length of the normal SAN string must be 4 or 5"


NUMERAL: dict[int, str] = {1: "st", 2: "nd", 3: "rd"}


class IndexMessage:
    __slots__ = ["__index"]

    __index: int

    def __init__(self, index: int):
        self.__index = index

    def value(self) -> str:
        numeral: str = NUMERAL[self.__index] if self.__index in NUMERAL.keys() else "th"
        return f"At the {self.__index}{numeral} element: "
