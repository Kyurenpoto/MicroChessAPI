# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, NamedTuple

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


class Piece(NamedTuple):
    symbol: str

    def color(self) -> str:
        return PIECE_COLOR[self.symbol]


class PieceAt(NamedTuple):
    board: BoardString
    square: Square

    def value(self) -> Piece:
        file_val: int = ord(self.square.file()) - ord("a")
        rank_val: int = ord(self.square.rank()) - ord("1")

        return Piece(self.board.value()[file_val + ((7 - rank_val) * 8)])
