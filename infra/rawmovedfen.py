# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, NamedTuple

import chess

CASTLING_PART_TRANSFORM: Final[dict[tuple[str, str], str]] = {
    ("w", "Kk"): "k",
    ("w", "K"): "-",
    ("w", "k"): "k",
    ("w", "-"): "-",
    ("b", "Kk"): "K",
    ("b", "K"): "K",
    ("b", "k"): "-",
    ("b", "-"): "-",
}


class TransformedCastlingPart(NamedTuple):
    turn: str
    castling: str
    piece: str

    def value(self) -> str:
        return CASTLING_PART_TRANSFORM[(self.turn, self.castling)] if self.piece in "KkRr" else self.castling


class RawMovedFen(NamedTuple):
    fen: str
    san: str

    def __str__(self) -> str:
        origin: list[str] = self.fen.split(" ")

        board: chess.Board = chess.Board(self.fen)
        move: chess.Move = board.parse_san(self.san)
        piece: str = board.piece_at(move.from_square).symbol()
        board.push(move)

        moved: list[str] = board.fen().split(" ")

        return " ".join(moved[:2] + [TransformedCastlingPart(origin[1], origin[2], piece).value()] + moved[3:])
