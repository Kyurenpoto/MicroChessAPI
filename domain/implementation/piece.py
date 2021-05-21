# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final

from .boardstring import BoardString
from .square import Square

BLACK_PIECES: Final[str] = "pkqrnb"
WHITE_PIECES: Final[str] = "PKQRNB"
PIECE_COLOR: Final[dict[str, str]] = {
    "P": "w",
    "K": "w",
    "Q": "w",
    "R": "w",
    "N": "w",
    "B": "w",
    "p": "b",
    "k": "b",
    "q": "b",
    "r": "b",
    "n": "b",
    "b": "b",
}


class Piece:
    __slots__ = ["__symbol"]

    __symbol: str

    def __init__(self, symbol: str):
        self.__symbol = symbol

    def symbol(self) -> str:
        return self.__symbol

    def color(self) -> str:
        return PIECE_COLOR[self.__symbol]


class PieceAt:
    __slots__ = ["__board", "__square"]

    __board: BoardString
    __square: Square

    def __init__(self, board: BoardString, square: Square):
        self.__board = board
        self.__square = square

    def value(self) -> Piece:
        file_val: int = ord(self.__square.file()) - ord("a")
        rank_val: int = ord(self.__square.rank()) - ord("1")

        return Piece(self.__board.value()[file_val + ((7 - rank_val) * 8)])
