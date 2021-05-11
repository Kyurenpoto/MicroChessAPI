# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List

from .microboard import MovedMicroBoard
from .worktarget import ValidWorkTarget, WorkTarget


class WorkResult:
    __slots__ = ["__target"]

    __target: WorkTarget

    def __init__(self, target: WorkTarget):
        self.__target = target

    def value(self) -> str:
        return str(MovedMicroBoard(self.__target.fen(), self.__target.san()).value().fen())


class CreatedWorkResult:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> str:
        return WorkResult(ValidWorkTarget(WorkTarget(self.__index, self.__fens, self.__sans)).value()).value()
