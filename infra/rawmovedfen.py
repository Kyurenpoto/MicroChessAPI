# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, Final, List, Optional, Tuple

import chess
from domain.error.microboarderror import (
    MSG_CANNOT_CASTLE,
    MSG_EMPTY_FROM_SQUARE,
    MSG_FULL_TO_SQUARE,
    MSG_INVALID_PIECE_MOVE,
    MSG_OPPOSITE_FROM_SQUARE,
)
from domain.implementation.mappable import Mappable

CASTLING_SAN: Final[str] = "O-O"


class RawCastlableSAN:
    __slots__ = ["__board", "__san"]

    __board: chess.Board
    __san: str

    def __init__(self, board: chess.Board, san: str):
        self.__board = board
        self.__san = san

    def value(self) -> str:
        if len(list(filter(lambda x: self.__board.is_castling(x), self.__board.legal_moves))) == 0:
            raise RuntimeError(MSG_CANNOT_CASTLE)

        return self.__san


class RawValidFromSquarePieceSAN:
    __slots__ = ["__board", "__san"]

    __board: chess.Board
    __san: str

    def __init__(self, board: chess.Board, san: str):
        self.__board = board
        self.__san = san

    def value(self) -> str:
        move: chess.Move = chess.Move.from_uci(self.__san)
        from_piece: Optional[chess.Piece] = self.__board.piece_at(move.from_square)
        if from_piece is None:
            raise RuntimeError(MSG_EMPTY_FROM_SQUARE)
        if from_piece.color != self.__board.turn:
            raise RuntimeError(MSG_OPPOSITE_FROM_SQUARE)

        return self.__san


class RawValidToSquarePieceSAN:
    __slots__ = ["__board", "__san"]

    __board: chess.Board
    __san: str

    def __init__(self, board: chess.Board, san: str):
        self.__board = board
        self.__san = san

    def value(self) -> str:
        move: chess.Move = chess.Move.from_uci(self.__san)
        to_piece: Optional[chess.Piece] = self.__board.piece_at(move.to_square)
        if to_piece is not None and to_piece.color == self.__board.turn:
            raise RuntimeError(MSG_FULL_TO_SQUARE)

        return self.__san


class RawValidPieceMoveSAN:
    __slots__ = ["__board", "__san"]

    __board: chess.Board
    __san: str

    def __init__(self, board: chess.Board, san: str):
        self.__board = board
        self.__san = san

    def value(self) -> str:
        move: chess.Move = chess.Move.from_uci(self.__san)
        if move not in self.__board.legal_moves:
            raise RuntimeError(MSG_INVALID_PIECE_MOVE)

        return self.__san


class RawValidMove:
    __slots__ = ["__board", "__san"]

    __board: chess.Board
    __san: str

    def __init__(self, board: chess.Board, san: str):
        self.__board = board
        self.__san = san

    def value(self) -> chess.Move:
        return self.__board.parse_san(
            RawCastlableSAN(self.__board, self.__san).value()
            if self.__san == CASTLING_SAN
            else Mappable(RawValidFromSquarePieceSAN(self.__board, self.__san).value())
            .mapped(lambda x: RawValidToSquarePieceSAN(self.__board, x).value())
            .mapped(lambda x: RawValidPieceMoveSAN(self.__board, x).value())
            .value()
        )


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
        move: chess.Move = RawValidMove(board, self.__san).value()
        piece: Optional[chess.Piece] = board.piece_at(move.from_square)
        board.push(move)

        moved: List[str] = board.fen().split(" ")

        return " ".join(
            moved[:2]
            + [CASTLING_PART_TRANSFORM[(origin[1], origin[2])] if piece.symbol() in "KkRr" else origin[2]]
            + moved[3:]
        )
