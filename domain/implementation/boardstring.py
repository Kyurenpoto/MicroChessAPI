# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, Final, List, Set

from domain.error.boardstringerror import (
    InvalidPieceNumber,
    InvalidRowNumber,
    InvalidSquareNumber,
    InvalidSymbol,
    NotEmptyOutside,
)

from .mappable import Mappable
from .microfen import MicroFEN

REPLACE_FOR_EXPAND: Dict[str, str] = {
    "1": ".",
    "2": "..",
    "3": "...",
    "4": "....",
    "5": ".....",
    "6": "......",
    "7": ".......",
    "8": "........",
    "/": "",
    "P": "P",
    "p": "p",
    "K": "K",
    "k": "k",
    "Q": "Q",
    "q": "q",
    "R": "R",
    "r": "r",
    "N": "N",
    "n": "n",
    "B": "B",
    "b": "b",
}


class BoardString:
    __slots__ = ["__fen", "__board"]

    __fen: MicroFEN
    __board: str

    def __init__(self, fen: MicroFEN):
        self.__fen = fen
        self.__board = ""

    def value(self) -> str:
        if self.__board == "":
            self.__board = "".join(map(lambda x: REPLACE_FOR_EXPAND[x], self.__fen.fen().split(" ")[0]))

        return self.__board

    def fen(self) -> MicroFEN:
        return self.__fen


class SymbolValidMicroBoardString:
    __slots__ = ["__board"]

    __board: BoardString

    def __init__(self, board: BoardString):
        self.__board = board

    def value(self) -> BoardString:
        fen: MicroFEN = self.__board.fen()
        board: Set[str] = set(fen.fen().split(" ")[0])
        max_valid: Set[str] = set(REPLACE_FOR_EXPAND.keys())
        if board & max_valid != board:
            raise RuntimeError(InvalidSymbol(fen.index(), fen.fens()).value())

        return self.__board


class SizeValidMicroBoardString:
    __slots__ = ["__board"]

    __board: BoardString

    def __init__(self, board: BoardString):
        self.__board = board

    def value(self) -> BoardString:
        fen: MicroFEN = self.__board.fen()
        splited: List[str] = fen.fen().split(" ")[0].split("/")
        if len(splited) != 8:
            raise RuntimeError(InvalidRowNumber(fen.index(), fen.fens()).value())
        for row in splited:
            if len("".join(map(lambda x: REPLACE_FOR_EXPAND[x], row))) != 8:
                raise RuntimeError(InvalidSquareNumber(fen.index(), fen.fens()).value())

        return self.__board


class EmptyOutsideMicroBoardString:
    __slots__ = ["__board"]

    __board: BoardString

    def __init__(self, board: BoardString):
        self.__board = board

    def value(self) -> BoardString:
        if (
            "".join([self.__board.value()[(i * 8) : (i * 8 + 4)] for i in range(0, 5)]) + self.__board.value()[40:]
            != "." * 44
        ):
            raise RuntimeError(NotEmptyOutside(self.__board.fen().index(), self.__board.fen().fens()).value())

        return self.__board


CHESS_PIECES: Final[str] = "KkQqPpRrBbNn"
PROMOTION_TO: Final[str] = "QqRrBbNn"
PROMOTION_FROM: Final[Dict[str, str]] = {
    "Q": "P",
    "q": "p",
    "R": "P",
    "r": "p",
    "N": "P",
    "n": "p",
    "B": "P",
    "b": "p",
}


class PieceRange:
    __slots__ = ["__min_val", "__max_val"]

    __min_val: int
    __max_val: int

    def __init__(self, a: int, b: int):
        self.__min_val = a
        self.__max_val = b

    def contained(self, x: int) -> bool:
        return self.__min_val <= x <= self.__max_val

    def max_val(self) -> int:
        return self.__max_val


MICROCHESS_PIECE_RANGES: Final[Dict[str, PieceRange]] = dict(
    zip(
        CHESS_PIECES,
        ([PieceRange(1, 1)] * 2) + ([PieceRange(0, 1)] * 4) + ([PieceRange(0, 2)] * 6),
    )
)


class PieceCountValidMicroBoardString:
    __slots__ = ["__board"]

    __board: BoardString

    def __init__(self, board: BoardString):
        self.__board = board

    def value(self) -> BoardString:
        board: str = self.__board.value().replace(".", "")
        for i in CHESS_PIECES:
            if not MICROCHESS_PIECE_RANGES[i].contained(board.count(i)):
                raise RuntimeError(InvalidPieceNumber(self.__board.fen().index(), self.__board.fen().fens()).value())

        for i in PROMOTION_TO:
            if board.count(i) + board.count(PROMOTION_FROM[i]) > MICROCHESS_PIECE_RANGES[i].max_val():
                raise RuntimeError(InvalidPieceNumber(self.__board.fen().index(), self.__board.fen().fens()).value())

        return self.__board


class ValidMicroBoardString:
    __slots__ = ["__board"]

    __board: BoardString

    def __init__(self, board: BoardString):
        self.__board = board

    def value(self) -> BoardString:
        return (
            Mappable(SymbolValidMicroBoardString(self.__board).value())
            .mapped(lambda x: SizeValidMicroBoardString(x).value())
            .mapped(lambda x: EmptyOutsideMicroBoardString(x).value())
            .mapped(lambda x: PieceCountValidMicroBoardString(x).value())
            .value()
        )
