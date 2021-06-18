# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from src.domain.error.createderror import CreatedErrorResponse
from src.domain.implementation.numeralmessage import NumeralMessage


class CannotCastle(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "movetarget.CannotCastleError"

    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> CannotCastle:
        return CannotCastle(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "Castling is only possible "
                + "when FEN's castling availability is active and between king and rook is empty"
            ),
            "fens, sans",
            [fens, sans],
            CannotCastle.error_type(),
        )


class EmptyFromSquare(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "movetarget.EmptyFromSquareError"

    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> EmptyFromSquare:
        return EmptyFromSquare(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "An active color piece should be placed on the from-square of SAN"
            ),
            "fens, sans",
            [fens, sans],
            EmptyFromSquare.error_type(),
        )


class OppositeFromSquare(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "movetarget.OppositeFromSquareError"

    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> OppositeFromSquare:
        return OppositeFromSquare(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "An active color piece should be placed on the from-square of SAN"
            ),
            "fens, sans",
            [fens, sans],
            OppositeFromSquare.error_type(),
        )


class FullToSquare(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "movetarget.FullToSquareError"

    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> FullToSquare:
        return FullToSquare(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "The to-square of SAN must be empty or place an inactive color piece"
            ),
            "fens, sans",
            [fens, sans],
            FullToSquare.error_type(),
        )


class InvalidPieceMove(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "movetarget.InvalidPieceMoveError"

    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> InvalidPieceMove:
        return InvalidPieceMove(
            (
                NumeralMessage.from_index_starting_zero(index)
                + "An piece located on the from-square of SAN cannot be moved to the to-square of SAN"
            ),
            "fens, sans",
            [fens, sans],
            InvalidPieceMove.error_type(),
        )
