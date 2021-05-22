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

REPLACE_FOR_EXPAND: Final[dict[str, str]] = {
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


MICROCHESS_SYMBOL: Final[set[str]] = set(REPLACE_FOR_EXPAND.keys())


def symbol_valid_micro_board_string(board: BoardString) -> BoardString:
    fen: MicroFEN = board.fen()
    symbol: set[str] = set(fen.fen().split(" ")[0])
    if symbol & MICROCHESS_SYMBOL != symbol:
        raise RuntimeError(InvalidSymbol.from_index_with_FENs(fen.index(), fen.fens()))

    return board


def size_valid_micro_board_string(board: BoardString) -> BoardString:
    fen: MicroFEN = board.fen()
    splited: list[str] = fen.fen().split(" ")[0].split("/")
    if len(splited) != 8:
        raise RuntimeError(InvalidRowNumber.from_index_with_FENs(fen.index(), fen.fens()))
    for row in splited:
        if len("".join(map(lambda x: REPLACE_FOR_EXPAND[x], row))) != 8:
            raise RuntimeError(InvalidSquareNumber.from_index_with_FENs(fen.index(), fen.fens()))

    return board


EMPTY_BOARDSTRING: Final[str] = "." * 44


def empty_outside_micro_board_string(board: BoardString) -> BoardString:
    if "".join([board.value()[i : i + 4] for i in range(0, 40, 8)]) + board.value()[40:] != EMPTY_BOARDSTRING:
        raise RuntimeError(NotEmptyOutside.from_index_with_FENs(board.fen().index(), board.fen().fens()))

    return board


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


def piece_count_valid_micro_board_string(board: BoardString) -> BoardString:
    piece: str = board.value().replace(".", "")
    for i in CHESS_PIECES:
        if not MICROCHESS_PIECE_RANGES[i].contained(piece.count(i)):
            raise RuntimeError(InvalidPieceNumber.from_index_with_FENs(board.fen().index(), board.fen().fens()))

    for i in PROMOTION_TO:
        if piece.count(i) + piece.count(PROMOTION_FROM[i]) > MICROCHESS_PIECE_RANGES[i].max_val:
            raise RuntimeError(InvalidPieceNumber.from_index_with_FENs(board.fen().index(), board.fen().fens()))

    return board


def valid_micro_board_string(board: BoardString) -> BoardString:
    return (
        Mappable(symbol_valid_micro_board_string(board))
        .mapped(lambda x: size_valid_micro_board_string(x))
        .mapped(lambda x: empty_outside_micro_board_string(x))
        .mapped(lambda x: piece_count_valid_micro_board_string(x))
        .value()
    )
