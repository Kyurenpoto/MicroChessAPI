# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List, Tuple

from domain.error.microboarderror import (
    MSG_CANNOT_CASTLE,
    MSG_EMPTY_FROM_SQUARE,
    MSG_FULL_TO_SQUARE,
    MSG_INVALID_PIECE_MOVE,
    MSG_OPPOSITE_FROM_SQUARE,
    CannotCastle,
    EmptyFromSquare,
    FullToSquare,
    InvalidPieceMove,
    OppositeFromSquare,
)

from .boardstring import FEN
from .fenstatus import FENStatus
from .legalsan import LegalSANs
from .microboard import MovedMicroBoard
from .microsan import SAN


class MovedFEN:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> str:
        try:
            return str(MovedMicroBoard(FEN(self.__fens[self.__index]), SAN(self.__sans[self.__index])).value().fen())
        except RuntimeError as ex:
            if ex.args[0] == MSG_CANNOT_CASTLE:
                raise RuntimeError(CannotCastle(self.__index, self.__fens, self.__sans).value()) from ex
            if ex.args[0] == MSG_EMPTY_FROM_SQUARE:
                raise RuntimeError(EmptyFromSquare(self.__index, self.__fens, self.__sans).value()) from ex
            if ex.args[0] == MSG_OPPOSITE_FROM_SQUARE:
                raise RuntimeError(OppositeFromSquare(self.__index, self.__fens, self.__sans).value()) from ex
            if ex.args[0] == MSG_FULL_TO_SQUARE:
                raise RuntimeError(FullToSquare(self.__index, self.__fens, self.__sans).value()) from ex
            if ex.args[0] == MSG_INVALID_PIECE_MOVE:
                raise RuntimeError(InvalidPieceMove(self.__index, self.__fens, self.__sans).value()) from ex
            raise ex


class MovedBoards:
    __slots__ = ["__fens", "__sans"]

    __fens: List[str]
    __sans: List[str]

    def __init__(self, fens: List[str], sans: List[str]):
        self.__fens = fens
        self.__sans = sans

    def value(self) -> List[str]:
        return [MovedFEN(index, self.__fens, self.__sans).value() for index in range(len(self.__fens))]


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
