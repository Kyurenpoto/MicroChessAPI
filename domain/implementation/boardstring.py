# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, NamedTuple

from domain.error.boardstringerror import (
    InvalidPieceNumber,
    InvalidRowNumber,
    InvalidSquareNumber,
    InvalidSymbol,
    NotEmptyOutside,
)

from .mappable import Mappable
from .microfen import MicroFEN

REPLACE_FOR_EXPAND: dict[str, str] = {
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


class SymbolValidMicroBoardString(NamedTuple):
    board: BoardString

    def value(self) -> BoardString:
        fen: MicroFEN = self.board.fen()
        board: set[str] = set(fen.fen().split(" ")[0])
        max_valid: set[str] = set(REPLACE_FOR_EXPAND.keys())
        if board & max_valid != board:
            raise RuntimeError(InvalidSymbol(fen.index(), fen.fens()).value())

        return self.board


class SizeValidMicroBoardString(NamedTuple):
    board: BoardString

    def value(self) -> BoardString:
        fen: MicroFEN = self.board.fen()
        splited: list[str] = fen.fen().split(" ")[0].split("/")
        if len(splited) != 8:
            raise RuntimeError(InvalidRowNumber(fen.index(), fen.fens()).value())
        for row in splited:
            if len("".join(map(lambda x: REPLACE_FOR_EXPAND[x], row))) != 8:
                raise RuntimeError(InvalidSquareNumber(fen.index(), fen.fens()).value())

        return self.board


class EmptyOutsideMicroBoardString(NamedTuple):
    board: BoardString

    def value(self) -> BoardString:
        if (
            "".join([self.board.value()[(i * 8) : (i * 8 + 4)] for i in range(0, 5)]) + self.board.value()[40:]
            != "." * 44
        ):
            raise RuntimeError(NotEmptyOutside(self.board.fen().index(), self.board.fen().fens()).value())

        return self.board


CHESS_PIECES: Final[str] = "KkQqPpRrBbNn"
PROMOTION_TO: Final[str] = "QqRrBbNn"
PROMOTION_FROM: Final[dict[str, str]] = {
    "Q": "P",
    "q": "p",
    "R": "P",
    "r": "p",
    "N": "P",
    "n": "p",
    "B": "P",
    "b": "p",
}


class PieceRange(NamedTuple):
    min_val: int
    max_val: int

    def contained(self, x: int) -> bool:
        return self.min_val <= x <= self.max_val


MICROCHESS_PIECE_RANGES: Final[dict[str, PieceRange]] = dict(
    zip(
        CHESS_PIECES,
        ([PieceRange(1, 1)] * 2) + ([PieceRange(0, 1)] * 4) + ([PieceRange(0, 2)] * 6),
    )
)


class PieceCountValidMicroBoardString(NamedTuple):
    board: BoardString

    def value(self) -> BoardString:
        board: str = self.board.value().replace(".", "")
        for i in CHESS_PIECES:
            if not MICROCHESS_PIECE_RANGES[i].contained(board.count(i)):
                raise RuntimeError(InvalidPieceNumber(self.board.fen().index(), self.board.fen().fens()).value())

        for i in PROMOTION_TO:
            if board.count(i) + board.count(PROMOTION_FROM[i]) > MICROCHESS_PIECE_RANGES[i].max_val:
                raise RuntimeError(InvalidPieceNumber(self.board.fen().index(), self.board.fen().fens()).value())

        return self.board


class ValidMicroBoardString(NamedTuple):
    board: BoardString

    def value(self) -> BoardString:
        return (
            Mappable(SymbolValidMicroBoardString(self.board).value())
            .mapped(lambda x: SizeValidMicroBoardString(x).value())
            .mapped(lambda x: EmptyOutsideMicroBoardString(x).value())
            .mapped(lambda x: PieceCountValidMicroBoardString(x).value())
            .value()
        )
