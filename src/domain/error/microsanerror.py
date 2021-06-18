# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from src.domain.error.createderror import CreatedErrorResponse
from src.domain.implementation.numeralmessage import NumeralMessage


class InvalidLength(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "microsan.InvalidLengthError"

    @classmethod
    def from_index_with_SANs(cls, index: int, sans: list[str]) -> InvalidLength:
        return InvalidLength(
            (NumeralMessage.from_index_starting_zero(index) + "The length of the normal SAN string must be 4 or 5"),
            "sans",
            sans,
            InvalidLength.error_type(),
        )


class InvalidFromSquare(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "microsan.InvalidFromSquareError"

    @classmethod
    def from_index_with_SANs(cls, index: int, sans: list[str]) -> InvalidFromSquare:
        return InvalidFromSquare(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "Only files e to h and ranks 4 to 8 are used in MicroChess"
            ),
            "sans",
            sans,
            InvalidFromSquare.error_type(),
        )


class InvalidToSquare(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "microsan.InvalidToSquareError"

    @classmethod
    def from_index_with_SANs(cls, index: int, sans: list[str]) -> InvalidToSquare:
        return InvalidToSquare(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "Only files e to h and ranks 4 to 8 are used in MicroChess"
            ),
            "sans",
            sans,
            InvalidToSquare.error_type(),
        )


class InvalidPromotion(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "microsan.InvalidPromotionError"

    @classmethod
    def from_index_with_SANs(cls, index: int, sans: list[str]) -> InvalidPromotion:
        return InvalidPromotion(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "Pawn can only promote to Queen, Rook, Knight, and Bishop"
            ),
            "sans",
            sans,
            InvalidPromotion.error_type(),
        )
