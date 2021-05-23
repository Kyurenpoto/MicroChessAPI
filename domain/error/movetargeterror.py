# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.modeldto import ModelErrorResponse
from domain.implementation.numeralmessage import NumeralMessage


class CannotCastle:
    @classmethod
    def msg(cls, index: int) -> str:
        return (
            NumeralMessage.from_index_starting_zero(index)
            + "Castling is only possible when FEN's castling availability is active and between king and rook is empty"
        )

    @classmethod
    def error_type(cls) -> str:
        return "movetarget.CannotCastleError"

    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=CannotCastle.msg(index),
            location="body",
            param="fens, sans",
            value=[fens, sans],
            error=CannotCastle.error_type(),
        )


class EmptyFromSquare:
    @classmethod
    def msg(cls, index: int) -> str:
        return (
            NumeralMessage.from_index_starting_zero(index)
            + "An active color piece should be placed on the from-square of SAN"
        )

    @classmethod
    def error_type(cls) -> str:
        return "movetarget.EmptyFromSquareError"

    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=EmptyFromSquare.msg(index),
            location="body",
            param="fens, sans",
            value=[fens, sans],
            error=EmptyFromSquare.error_type(),
        )


class OppositeFromSquare:
    @classmethod
    def msg(cls, index: int) -> str:
        return (
            NumeralMessage.from_index_starting_zero(index)
            + "An active color piece should be placed on the from-square of SAN"
        )

    @classmethod
    def error_type(cls) -> str:
        return "movetarget.OppositeFromSquareError"

    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=OppositeFromSquare.msg(index),
            location="body",
            param="fens, sans",
            value=[fens, sans],
            error=OppositeFromSquare.error_type(),
        )


class FullToSquare:
    @classmethod
    def msg(cls, index: int) -> str:
        return (
            NumeralMessage.from_index_starting_zero(index)
            + "The to-square of SAN must be empty or place an inactive color piece"
        )

    @classmethod
    def error_type(cls) -> str:
        return "movetarget.FullToSquareError"

    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=FullToSquare.msg(index),
            location="body",
            param="fens, sans",
            value=[fens, sans],
            error=FullToSquare.error_type(),
        )


class InvalidPieceMove:
    @classmethod
    def msg(cls, index: int) -> str:
        return (
            NumeralMessage.from_index_starting_zero(index)
            + "An piece located on the from-square of SAN cannot be moved to the to-square of SAN"
        )

    @classmethod
    def error_type(cls) -> str:
        return "movetarget.InvalidPieceMoveError"

    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=InvalidPieceMove.msg(index),
            location="body",
            param="fens, sans",
            value=[fens, sans],
            error=InvalidPieceMove.error_type(),
        )
