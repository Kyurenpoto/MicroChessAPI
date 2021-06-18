# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from src.domain.error.createderror import CreatedErrorResponse
from src.domain.implementation.numeralmessage import NumeralMessage


class NotEmptyOutside(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "boardstring.NotEmptyOutsideError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> NotEmptyOutside:
        return NotEmptyOutside(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "All outside the MicroChess area in the board part of FEN should be blank"
            ),
            "fens",
            fens,
            NotEmptyOutside.error_type(),
        )


class InvalidPieceNumber(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "boardstring.InvalidPieceNumberError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> InvalidPieceNumber:
        return InvalidPieceNumber(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "Only one King, a maximum of 1 Queen and Pawn, and a maximum of 2 Rooks, Bishops, and Nights"
                + " should exist in the board part"
            ),
            "fens",
            fens,
            InvalidPieceNumber.error_type(),
        )
