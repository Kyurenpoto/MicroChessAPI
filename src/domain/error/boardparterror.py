# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from src.domain.error.createderror import CreatedErrorResponse
from src.domain.implementation.numeralmessage import NumeralMessage


class InvalidSymbol(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "boardpart.InvalidSymbolError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> InvalidSymbol:
        return InvalidSymbol(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "The board part of the FEN should contain "
                + "only the numbers 1~8, '/', and symbols representing chess pieces"
            ),
            "fens",
            fens,
            InvalidSymbol.error_type(),
        )


class InvalidRowNumber(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "boardpart.InvalidRowNumberError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> InvalidRowNumber:
        return InvalidRowNumber(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "The board part of the FEN should contain "
                + "only The board part of FEN should have 8 rows separated by '/'"
            ),
            "fens",
            fens,
            InvalidRowNumber.error_type(),
        )


class InvalidSquareNumber(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "boardpart.InvalidSquareNumberError"

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> InvalidSquareNumber:
        return InvalidSquareNumber(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "Each row in the board part of FEN should contain 8 squares, including a blank and a piece"
            ),
            "fens",
            fens,
            InvalidSquareNumber.error_type(),
        )
