# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only


from typing import NamedTuple, Optional

from domain.error.movetargeterror import (
    CannotCastle,
    EmptyFromSquare,
    FullToSquare,
    InvalidPieceMove,
    OppositeFromSquare,
)
from domain.implementation.validmicrofen import ValidMicroFEN

from .basictype import FEN, SAN
from .boardstring import BoardString
from .legalsan import LegalSANs
from .mappable import Mappable
from .microfen import MicroFEN, MirroredMicroFEN
from .microsan import MicroSAN
from .piece import Piece, PieceAt
from .square import FromSquare, ToSquare
from .validmicrosan import MICRO_CASTLING_SAN, ValidMicroSAN


class MoveTarget:
    __slots__ = ["__index", "__fens", "__sans", "__fen", "__san"]

    __index: int
    __fens: list[str]
    __sans: list[str]
    __fen: Optional[MicroFEN]
    __san: Optional[MicroSAN]

    def __init__(self, index: int, fens: list[str], sans: list[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans
        self.__fen = None
        self.__san = None

    def value(self) -> tuple[int, list[str], list[str]]:
        return self.__index, self.__fens, self.__sans

    def microfen(self) -> MicroFEN:
        if self.__fen is None:
            self.__fen = ValidMicroFEN.from_MicroFEN(MicroFEN(self.__index, self.__fens))

        return self.__fen

    def microsan(self) -> MicroSAN:
        if self.__san is None:
            self.__san = ValidMicroSAN(MicroSAN(self.__index, self.__sans)).value()

        return self.__san

    def fen(self) -> FEN:
        return self.microfen().fen()

    def san(self) -> SAN:
        return self.microsan().san()


class CastlableMoveTarget(NamedTuple):
    target: MoveTarget

    def value(self) -> MoveTarget:
        if MICRO_CASTLING_SAN not in LegalSANs.from_FEN(
            self.target.fen() if self.target.fen().split(" ")[1] == "b" else MirroredMicroFEN(self.target.fen()).value()
        ):
            raise RuntimeError(CannotCastle.from_index_with_FENs_SANs(*(self.target.value())))

        return self.target


class FromSquarePieceValidMoveTarget(NamedTuple):
    target: MoveTarget

    def value(self) -> MoveTarget:
        piece: Piece = PieceAt(BoardString(self.target.microfen()), FromSquare(self.target.san())).value()
        if piece.symbol == ".":
            raise RuntimeError(EmptyFromSquare.from_index_with_FENs_SANs(*(self.target.value())))
        if piece.color() != self.target.fen().split(" ")[1]:
            raise RuntimeError(OppositeFromSquare.from_index_with_FENs_SANs(*(self.target.value())))

        return self.target


class ToSquarePieceValidMoveTarget(NamedTuple):
    target: MoveTarget

    def value(self) -> MoveTarget:
        piece: Piece = PieceAt(BoardString(self.target.microfen()), ToSquare(self.target.san())).value()
        if piece.symbol != "." and piece.color() == self.target.fen().split(" ")[1]:
            raise RuntimeError(FullToSquare.from_index_with_FENs_SANs(*(self.target.value())))

        return self.target


class LegalMoveMoveTarget(NamedTuple):
    target: MoveTarget

    def value(self) -> MoveTarget:
        if self.target.san() not in LegalSANs.from_FEN(self.target.fen()):
            raise RuntimeError(InvalidPieceMove.from_index_with_FENs_SANs(*(self.target.value())))

        return self.target


class ValidMoveTarget(NamedTuple):
    target: MoveTarget

    def value(self) -> MoveTarget:
        return (
            CastlableMoveTarget(self.target).value()
            if self.target.san() == MICRO_CASTLING_SAN
            else (
                Mappable(FromSquarePieceValidMoveTarget(self.target).value())
                .mapped(lambda x: ToSquarePieceValidMoveTarget(x).value())
                .mapped(lambda x: LegalMoveMoveTarget(x).value())
                .value()
            )
        )
