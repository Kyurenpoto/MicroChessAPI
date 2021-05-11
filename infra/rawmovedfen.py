# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, Final, List, Tuple

import chess

CASTLING_PART_TRANSFORM: Final[Dict[Tuple[str, str], str]] = {
    ("w", "Kk"): "k",
    ("w", "K"): "-",
    ("w", "k"): "k",
    ("w", "-"): "-",
    ("b", "Kk"): "K",
    ("b", "K"): "K",
    ("b", "k"): "-",
    ("b", "-"): "-",
}


class TransformedCastlingPart:
    __slots__ = ["__turn", "__castling", "__piece"]

    __turn: str
    __castling: str
    __piece: str

    def __init__(self, turn: str, castling: str, piece: str):
        self.__turn = turn
        self.__castling = castling
        self.__piece = piece

    def value(self) -> str:
        return CASTLING_PART_TRANSFORM[(self.__turn, self.__castling)] if self.__piece in "KkRr" else self.__castling


class RawMovedFen:
    __slots__ = ["__fen", "__san"]

    __fen: str
    __san: str

    def __init__(self, fen: str, san: str):
        self.__fen = fen
        self.__san = san

    def __str__(self) -> str:
        origin: List[str] = self.__fen.split(" ")

        board: chess.Board = chess.Board(self.__fen)
        move: chess.Move = board.parse_san(self.__san)
        piece: str = board.piece_at(move.from_square).symbol()
        board.push(move)

        moved: List[str] = board.fen().split(" ")

        return " ".join(moved[:2] + [TransformedCastlingPart(origin[1], origin[2], piece).value()] + moved[3:])
