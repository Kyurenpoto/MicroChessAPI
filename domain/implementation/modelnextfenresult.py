# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List

from .workresult import CreatedWorkResult


class MovedBoards:
    __slots__ = ["__fens", "__sans"]

    __fens: List[str]
    __sans: List[str]

    def __init__(self, fens: List[str], sans: List[str]):
        self.__fens = fens
        self.__sans = sans

    def value(self) -> List[str]:
        return [CreatedWorkResult(index, self.__fens, self.__sans).value() for index in range(len(self.__fens))]


class ModelNextFENResult:
    __slots__ = ["__fens", "__sans"]

    __fens: List[str]
    __sans: List[str]

    def __init__(self, fens: List[str], sans: List[str]):
        self.__fens = fens
        self.__sans = sans

    def value(self) -> List[str]:
        return MovedBoards(self.__fens, self.__sans).value()
