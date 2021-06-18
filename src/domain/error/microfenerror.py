# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from src.domain.error.createderror import CreatedErrorResponse
from src.domain.implementation.numeralmessage import NumeralMessage


class InvalidStructure(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidStructureError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> InvalidStructure:
        return InvalidStructure(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "The FEN should consist of 6 parts separated by spaces: "
                + "'[Board part] [Turn part] [Castling part] [Enpassant part] [Halfmove part] [Fullmove part]'"
            ),
            "fens",
            fens,
            InvalidStructure.error_type(),
        )


class InvalidTurnPart(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidTurnPartError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> InvalidTurnPart:
        return InvalidTurnPart(
            NumeralMessage.from_index_starting_zero(index) + "Turn part of FEN should be one of 'w', 'b'",
            "fens",
            fens,
            InvalidTurnPart.error_type(),
        )


class InvalidCastlingPart(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidCastlingPartError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> InvalidCastlingPart:
        return InvalidCastlingPart(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "Castling part of FEN should be one of 'Kk', 'K', 'k', or '-'"
            ),
            "fens",
            fens,
            InvalidCastlingPart.error_type(),
        )


class InvalidEnpassantPart(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidEnpassantPartError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> InvalidEnpassantPart:
        return InvalidEnpassantPart(
            NumeralMessage.from_index_starting_zero(index) + "Enpassant part of FEN should be '-'",
            "fens",
            fens,
            InvalidEnpassantPart.error_type(),
        )


class InvalidHalfmovePart(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidHalfmovePartError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> InvalidHalfmovePart:
        return InvalidHalfmovePart(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "Halfmove part of FEN should be an integer in range [0, 50]"
            ),
            "fens",
            fens,
            InvalidHalfmovePart.error_type(),
        )


class InvalidFullmovePart(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidFullmovePartError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> InvalidFullmovePart:
        return InvalidFullmovePart(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "Fullmove part of FEN should be an integer in range [1, 80]"
            ),
            "fens",
            fens,
            InvalidFullmovePart.error_type(),
        )
