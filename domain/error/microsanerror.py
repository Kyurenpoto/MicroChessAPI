# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final

from domain.dto.modeldto import ModelErrorResponse
from domain.implementation.indexmessage import IndexMessage

from .errorbase import IndexedSANsError

MSG_INVALID_LENGTH: Final[str] = "The length of the normal SAN string must be 4 or 5"
MSG_INVALID_FROM_SQUARE: Final[str] = "Only files e to h and ranks 4 to 8 are used in MicroChess"
MSG_INVALID_TO_SQUARE: Final[str] = "Only files e to h and ranks 4 to 8 are used in MicroChess"
MSG_INVALID_PROMOTION: Final[str] = "Pawn can only promote to Queen, Rook, Knight, and Bishop"
ERROR_TYPE_INVALID_LENGTH: Final[str] = "microsan.InvalidLengthError"
ERROR_TYPE_INVALID_FROM_SQUARE: Final[str] = "microsan.InvalidFromSquareError"
ERROR_TYPE_INVALID_TO_SQUARE: Final[str] = "microsan.InvalidToSquareError"
ERROR_TYPE_INVALID_PROMOTION: Final[str] = "microsan.InvalidPromotionError"


class InvalidLength(IndexedSANsError):
    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.index).value() + MSG_INVALID_LENGTH,
            location="body",
            param="sans",
            value=self.sans,
            error=ERROR_TYPE_INVALID_LENGTH,
        )


class InvalidFromSquare(IndexedSANsError):
    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.index).value() + MSG_INVALID_FROM_SQUARE,
            location="body",
            param="sans",
            value=self.sans,
            error=ERROR_TYPE_INVALID_FROM_SQUARE,
        )


class InvalidToSquare(IndexedSANsError):
    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.index).value() + MSG_INVALID_TO_SQUARE,
            location="body",
            param="sans",
            value=self.sans,
            error=ERROR_TYPE_INVALID_TO_SQUARE,
        )


class InvalidPromotion(IndexedSANsError):
    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.index).value() + MSG_INVALID_PROMOTION,
            location="body",
            param="sans",
            value=self.sans,
            error=ERROR_TYPE_INVALID_PROMOTION,
        )
