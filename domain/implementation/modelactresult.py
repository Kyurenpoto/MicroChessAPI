# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List, Tuple

from .basictype import FEN
from .fenstatus import FENStatus
from .legalsan import LegalSANs
from .microboard import MovedMicroBoard
from .worktarget import ValidWorkTarget, WorkTarget


class WorkResult:
    __slots__ = ["__target"]

    __target: WorkTarget

    def __init__(self, target: WorkTarget):
        self.__target = target

    def value(self) -> str:
        return str(MovedMicroBoard(self.__target.fen(), self.__target.san()).value().fen())


class MovedBoards:
    __slots__ = ["__fens", "__sans"]

    __fens: List[str]
    __sans: List[str]

    def __init__(self, fens: List[str], sans: List[str]):
        self.__fens = fens
        self.__sans = sans

    def value(self) -> List[str]:
        return [
            WorkResult(ValidWorkTarget(WorkTarget(index, self.__fens, self.__sans)).value()).value()
            for index in range(len(self.__fens))
        ]


class LegalMoves:
    __slots__ = ["__moved_boards"]

    __moved_boards: List[str]

    def __init__(self, moved_boards: List[str]):
        self.__moved_boards = moved_boards

    def value(self) -> List[List[str]]:
        return [[str(san) for san in LegalSANs(FEN(fen)).value()] for fen in self.__moved_boards]


class Statuses:
    __slots__ = ["__moved_boards", "__legal_moves"]

    __moved_boards: List[str]
    __legal_moves: List[List[str]]

    def __init__(self, moved_boards: List[str], legal_moves: List[List[str]]):
        self.__moved_boards = moved_boards
        self.__legal_moves = legal_moves

    def value(self) -> List[int]:
        return [
            int(FENStatus(FEN(fen), len(moves)).value().value)
            for fen, moves in zip(self.__moved_boards, self.__legal_moves)
        ]


class ModelActResult:
    __slots__ = ["__fens", "__sans"]

    __fens: List[str]
    __sans: List[str]

    def __init__(self, fens: List[str], sans: List[str]):
        self.__fens = fens
        self.__sans = sans

    def value(self) -> Tuple[List[str], List[List[str]], List[int]]:
        moved_boards: List[str] = MovedBoards(self.__fens, self.__sans).value()
        legal_moves: List[List[str]] = LegalMoves(moved_boards).value()
        statuses: List[int] = Statuses(moved_boards, legal_moves).value()

        return moved_boards, legal_moves, statuses
