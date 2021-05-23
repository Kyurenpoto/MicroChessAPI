# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.modeldto import ModelErrorResponse
from domain.implementation.numeralmessage import NumeralMessage


class NotEmptyOutside:
    @classmethod
    def msg(cls, index: int) -> str:
        return (
            NumeralMessage.from_index(index)
            + "All outside the MicroChess area in the board part of FEN should be blank"
        )

    @classmethod
    def error_type(cls) -> str:
        return "boardstring.NotEmptyOutsideError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=NotEmptyOutside.msg(index),
            location="body",
            param="fens",
            value=fens,
            error=NotEmptyOutside.error_type(),
        )


class InvalidPieceNumber:
    @classmethod
    def msg(cls, index: int) -> str:
        return (
            NumeralMessage.from_index(index)
            + "Only one King, a maximum of 1 Queen and Pawn, and a maximum of 2 Rooks, Bishops, and Nights"
            + " should exist in the board part"
        )

    @classmethod
    def error_type(cls) -> str:
        return "boardstring.InvalidPieceNumberError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidPieceNumber.msg(index),
            location="body",
            param="fens",
            value=fens,
            error=InvalidPieceNumber.error_type(),
        )
