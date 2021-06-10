# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from src.domain.dto.modeldto import ModelErrorResponse
from src.domain.implementation.numeralmessage import NumeralMessage


class InvalidLength:
    @classmethod
    def msg(cls, index: int) -> str:
        return NumeralMessage.from_index_starting_zero(index) + "The length of the normal SAN string must be 4 or 5"

    @classmethod
    def error_type(cls) -> str:
        return "microsan.InvalidLengthError"

    @classmethod
    def from_index_with_SANs(cls, index: int, sans: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidLength.msg(index),
            location="body",
            param="sans",
            value=sans,
            error=InvalidLength.error_type(),
        )


class InvalidFromSquare:
    @classmethod
    def msg(cls, index: int) -> str:
        return (
            NumeralMessage.from_index_starting_zero(index) + "Only files e to h and ranks 4 to 8 are used in MicroChess"
        )

    @classmethod
    def error_type(cls) -> str:
        return "microsan.InvalidFromSquareError"

    @classmethod
    def from_index_with_SANs(cls, index: int, sans: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidFromSquare.msg(index),
            location="body",
            param="sans",
            value=sans,
            error=InvalidFromSquare.error_type(),
        )


class InvalidToSquare:
    @classmethod
    def msg(cls, index: int) -> str:
        return (
            NumeralMessage.from_index_starting_zero(index) + "Only files e to h and ranks 4 to 8 are used in MicroChess"
        )

    @classmethod
    def error_type(cls) -> str:
        return "microsan.InvalidToSquareError"

    @classmethod
    def from_index_with_SANs(cls, index: int, sans: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidToSquare.msg(index),
            location="body",
            param="sans",
            value=sans,
            error=InvalidToSquare.error_type(),
        )


class InvalidPromotion:
    @classmethod
    def msg(cls, index: int) -> str:
        return (
            NumeralMessage.from_index_starting_zero(index) + "Pawn can only promote to Queen, Rook, Knight, and Bishop"
        )

    @classmethod
    def error_type(cls) -> str:
        return "microsan.InvalidPromotionError"

    @classmethod
    def from_index_with_SANs(cls, index: int, sans: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidPromotion.msg(index),
            location="body",
            param="sans",
            value=sans,
            error=InvalidPromotion.error_type(),
        )
