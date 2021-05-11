# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, Final

from .basictype import FEN
from .mappable import Mappable

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

    __fen: FEN
    __board: str

    def __init__(self, fen: FEN):
        self.__fen = fen
        self.__board = ""

    def value(self) -> str:
        if self.__board == "":
            try:
                self.__board = "".join(map(lambda x: REPLACE_FOR_EXPAND[x], self.__fen.split(" ")[0]))
            except KeyError as ex:
                raise RuntimeError("Invalid symbol in board part") from ex

        return self.__board

    def fen(self) -> FEN:
        return self.__fen


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
            raise RuntimeError("Not empty outside of MicroChess board part")

        return self.__board


CHESS_PIECES: Final[str] = "KkQqPpRrBbNn"


class PieceRange:
    __slots__ = ["min_val", "max_val"]

    min_val: int
    max_val: int

    def __init__(self, a: int, b: int):
        self.min_val = a
        self.max_val = b

    def contained(self, x: int) -> bool:
        return self.min_val <= x <= self.max_val


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
                raise RuntimeError("The number of some pieces is invalid")

        return self.__board


class ValidMicroBoardString:
    __slots__ = ["__board"]

    __board: BoardString

    def __init__(self, board: BoardString):
        self.__board = board

    def value(self) -> BoardString:
        return (
            Mappable(EmptyOutsideMicroBoardString(self.__board).value())
            .mapped(lambda x: PieceCountValidMicroBoardString(x).value())
            .value()
        )
