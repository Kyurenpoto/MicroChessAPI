# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

import chess
from domain.implementation.splitablefen import ColorPart


class SymbolizableColorPart(ColorPart):
    @classmethod
    def from_FEN(cls, fen: str) -> SymbolizableColorPart:
        return SymbolizableColorPart(ColorPart.from_FEN(fen))

    def king(self) -> str:
        return {"w": "K", "b": "k"}[self]

    def spend_from(self, castling: str) -> str:
        return {"w": castling[1:], "b": castling[:-1]}[self] if self.king() in castling else castling


class CastlingPart(str):
    @classmethod
    def from_FEN(cls, fen: str) -> CastlingPart:
        return CastlingPart(fen.split(" ")[2])

    def correct(self) -> CastlingPart:
        return CastlingPart("-" if self == "" else self)

    def spend_castlable_piece(self, color: SymbolizableColorPart) -> CastlingPart:
        return CastlingPart(color.spend_from(self)).correct()

    def spend(self, color: SymbolizableColorPart, piece: str) -> CastlingPart:
        return self.spend_castlable_piece(color) if piece in "KkRr" else self

    def replace_from(self, fen: str) -> str:
        splited: list[str] = fen.split(" ")

        return " ".join(splited[:2] + [str(self)] + splited[3:])


class RawMovedFEN(str):
    @classmethod
    def from_trace_FEN_with_piece(cls, fen: str, next_fen: str, piece: str) -> RawMovedFEN:
        return RawMovedFEN(
            CastlingPart.from_FEN(fen).spend(SymbolizableColorPart.from_FEN(fen), piece).replace_from(next_fen)
        )

    @classmethod
    def from_FEN_SAN(cls, fen: str, san: str) -> RawMovedFEN:
        board: chess.Board = chess.Board(fen)
        move: chess.Move = board.parse_san(san)
        piece: str = board.piece_at(move.from_square).symbol()
        board.push(move)

        return RawMovedFEN.from_trace_FEN_with_piece(fen, board.fen(), piece)
