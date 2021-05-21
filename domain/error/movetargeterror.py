# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final

from domain.dto.modeldto import ModelErrorResponse
from domain.implementation.numeralmessage import NumeralMessage

from .errorbase import IndexedParamsError

MSG_CANNOT_CASTLE: Final[
    str
] = "Castling is only possible when FEN's castling availability is active and between king and rook is empty"
MSG_EMPTY_FROM_SQUARE: Final[str] = "An active color piece should be placed on the from-square of SAN"
MSG_OPPOSITE_FROM_SQUARE: Final[str] = "An active color piece should be placed on the from-square of SAN"
MSG_FULL_TO_SQUARE: Final[str] = "The to-square of SAN must be empty or place an inactive color piece"
MSG_INVALID_PIECE_MOVE: Final[
    str
] = "An piece located on the from-square of SAN cannot be moved to the to-square of SAN"
ERROR_TYPE_CANNOT_CASTLE: Final[str] = "movetarget.CannotCastleError"
ERROR_TYPE_EMPTY_FROM_SQUARE: Final[str] = "movetarget.EmptyFromSquareError"
ERROR_TYPE_OPPOSITE_FROM_SQUARE: Final[str] = "movetarget.OppositeFromSquareError"
ERROR_TYPE_FULL_TO_SQUARE: Final[str] = "movetarget.FullToSquareError"
ERROR_TYPE_INVALID_PIECE_MOVE: Final[str] = "movetarget.InvalidPieceMoveError"


class CannotCastle(IndexedParamsError):
    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=NumeralMessage.from_index(self.index) + MSG_CANNOT_CASTLE,
            location="body",
            param="fens, sans",
            value=[self.fens, self.sans],
            error=ERROR_TYPE_CANNOT_CASTLE,
        )


class EmptyFromSquare(IndexedParamsError):
    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=NumeralMessage.from_index(self.index) + MSG_EMPTY_FROM_SQUARE,
            location="body",
            param="fens, sans",
            value=[self.fens, self.sans],
            error=ERROR_TYPE_EMPTY_FROM_SQUARE,
        )


class OppositeFromSquare(IndexedParamsError):
    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=NumeralMessage.from_index(self.index) + MSG_OPPOSITE_FROM_SQUARE,
            location="body",
            param="fens, sans",
            value=[self.fens, self.sans],
            error=ERROR_TYPE_OPPOSITE_FROM_SQUARE,
        )


class FullToSquare(IndexedParamsError):
    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=NumeralMessage.from_index(self.index) + MSG_FULL_TO_SQUARE,
            location="body",
            param="fens, sans",
            value=[self.fens, self.sans],
            error=ERROR_TYPE_FULL_TO_SQUARE,
        )


class InvalidPieceMove(IndexedParamsError):
    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=NumeralMessage.from_index(self.index) + MSG_INVALID_PIECE_MOVE,
            location="body",
            param="fens, sans",
            value=[self.fens, self.sans],
            error=ERROR_TYPE_INVALID_PIECE_MOVE,
        )
