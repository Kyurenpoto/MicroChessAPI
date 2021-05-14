# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List

from domain.implementation.movedfen import MovedFEN
from domain.implementation.movetarget import MoveTarget, ValidMoveTarget


class NextFen:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> str:
        target: MoveTarget = ValidMoveTarget(MoveTarget(self.__index, self.__fens, self.__sans)).value()

        return str(MovedFEN(target.fen(), target.san()).value())


class ModelNextFENResult:
    __slots__ = ["__fens", "__sans"]

    __fens: List[str]
    __sans: List[str]

    def __init__(self, fens: List[str], sans: List[str]):
        self.__fens = fens
        self.__sans = sans

    def value(self) -> List[str]:
        return [NextFen(index, self.__fens, self.__sans).value() for index in range(len(self.__fens))]
