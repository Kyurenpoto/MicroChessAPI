# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.modeldto import ModelErrorResponse
from domain.implementation.numeralmessage import NumeralMessage


class InvalidStructure:
    @classmethod
    def msg(cls, index: int) -> str:
        return (
            NumeralMessage.from_index(index)
            + "The FEN should consist of 6 parts separated by spaces: "
            + "'[Board part] [Turn part] [Castling part] [Enpassant part] [Halfmove part] [Fullmove part]'"
        )

    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidStructureError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidStructure.msg(index),
            location="body",
            param="fens",
            value=fens,
            error=InvalidStructure.error_type(),
        )


class InvalidTurnPart:
    @classmethod
    def msg(cls, index: int) -> str:
        return NumeralMessage.from_index(index) + "Turn part of FEN should be one of 'w', 'b'"

    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidTurnPartError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidTurnPart.msg(index),
            location="body",
            param="fens",
            value=fens,
            error=InvalidTurnPart.error_type(),
        )


class InvalidCastlingPart:
    @classmethod
    def msg(cls, index: int) -> str:
        return NumeralMessage.from_index(index) + "Castling part of FEN should be one of 'Kk', 'K', 'k', or '-'"

    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidCastlingPartError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidCastlingPart.msg(index),
            location="body",
            param="fens",
            value=fens,
            error=InvalidCastlingPart.error_type(),
        )


class InvalidEnpassantPart:
    @classmethod
    def msg(cls, index: int) -> str:
        return NumeralMessage.from_index(index) + "Enpassant part of FEN should be '-'"

    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidEnpassantPartError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidEnpassantPart.msg(index),
            location="body",
            param="fens",
            value=fens,
            error=InvalidEnpassantPart.error_type(),
        )


class InvalidHalfmovePart:
    @classmethod
    def msg(cls, index: int) -> str:
        return NumeralMessage.from_index(index) + "Halfmove part of FEN should be an integer in range [0, 50]"

    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidHalfmovePartError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidHalfmovePart.msg(index),
            location="body",
            param="fens",
            value=fens,
            error=InvalidHalfmovePart.error_type(),
        )


class InvalidFullmovePart:
    @classmethod
    def msg(cls, index: int) -> str:
        return NumeralMessage.from_index(index) + "Fullmove part of FEN should be an integer in range [1, 80]"

    @classmethod
    def error_type(cls) -> str:
        return "microfen.InvalidFullmovePartError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidFullmovePart.msg(index),
            location="body",
            param="fens",
            value=fens,
            error=InvalidFullmovePart.error_type(),
        )
