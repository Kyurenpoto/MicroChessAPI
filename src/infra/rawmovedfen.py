# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

import chess
from src.domain.implementation.splitablefen import CastlingPart, ColorPart, ReplacableSplitedFEN


class SymbolizableColorPart(ColorPart):
    @classmethod
    def from_FEN(cls, fen: str) -> SymbolizableColorPart:
        return SymbolizableColorPart(ColorPart.from_FEN(fen))

    def king(self) -> str:
        return {"w": "K", "b": "k"}[self]

    def spend_from(self, castling: str) -> str:
        return {"w": castling[1:], "b": castling[:-1]}[self] if self.king() in castling else castling


class SpendableCastlingPart(CastlingPart):
    @classmethod
    def from_FEN(cls, fen: str) -> SpendableCastlingPart:
        return SpendableCastlingPart(CastlingPart.from_FEN(fen))

    def correct(self) -> SpendableCastlingPart:
        return SpendableCastlingPart("-" if self == "" else self)

    def spend_castlable_piece(self, color: SymbolizableColorPart) -> SpendableCastlingPart:
        return SpendableCastlingPart(color.spend_from(self)).correct()

    def spend(self, color: SymbolizableColorPart, piece: str) -> SpendableCastlingPart:
        return self.spend_castlable_piece(color) if piece in "KkRr" else self

    def replace_from(self, fen: str) -> str:
        return ReplacableSplitedFEN.from_FEN(fen).replace_castling(self).join_parts()


class RawMovedFEN(str):
    @classmethod
    def from_trace_FEN_with_piece(cls, fen: str, next_fen: str, piece: str) -> RawMovedFEN:
        return RawMovedFEN(
            SpendableCastlingPart.from_FEN(fen).spend(SymbolizableColorPart.from_FEN(fen), piece).replace_from(next_fen)
        )

    @classmethod
    def from_FEN_SAN(cls, fen: str, san: str) -> RawMovedFEN:
        board: chess.Board = chess.Board(fen)
        move: chess.Move = board.parse_san(san)
        piece: str = board.piece_at(move.from_square).symbol()
        board.push(move)

        return RawMovedFEN.from_trace_FEN_with_piece(fen, board.fen(), piece)
