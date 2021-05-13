# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only


from typing import List, Optional, Tuple

from domain.error.worktargeterror import (
    CannotCastle,
    EmptyFromSquare,
    FullToSquare,
    InvalidPieceMove,
    OppositeFromSquare,
)
from domain.implementation.microboard import CreatedMicroBoard

from .basictype import FEN, SAN
from .boardstring import BoardString
from .legalsan import LegalSANs
from .mappable import Mappable
from .microfen import MirroredMicroFEN
from .microsan import MicroSAN
from .piece import Piece, PieceAt
from .square import FromSquare, ToSquare
from .validmicrosan import MICRO_CASTLING_SAN, ValidMicroSAN


class WorkTarget:
    __slots__ = ["__index", "__fens", "__sans", "__fen", "__san"]

    __index: int
    __fens: List[str]
    __sans: List[str]
    __fen: FEN
    __san: Optional[MicroSAN]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans
        self.__fen = FEN("")
        self.__san = None

    def value(self) -> Tuple[int, List[str], List[str]]:
        return self.__index, self.__fens, self.__sans

    def fen(self) -> FEN:
        if self.__fen == FEN(""):
            self.__fen = CreatedMicroBoard(FEN(self.__fens[self.__index])).value().fen()

        return self.__fen

    def microsan(self) -> MicroSAN:
        if self.__san is None:
            self.__san = ValidMicroSAN(MicroSAN(self.__index, self.__sans)).value()

        return self.__san

    def san(self) -> SAN:
        return self.microsan().san()


class CastlableWorkTarget:
    __slots__ = ["__target"]

    __target: WorkTarget

    def __init__(self, target: WorkTarget):
        self.__target = target

    def value(self) -> WorkTarget:
        if (
            MICRO_CASTLING_SAN
            not in LegalSANs(
                self.__target.fen()
                if self.__target.fen().split(" ")[1] == "b"
                else MirroredMicroFEN(self.__target.fen()).value()
            ).value()
        ):
            raise RuntimeError(CannotCastle(*(self.__target.value())).value())

        return self.__target


class FromSquarePieceValidWorkTarget:
    __slots__ = ["__target"]

    __target: WorkTarget

    def __init__(self, target: WorkTarget):
        self.__target = target

    def value(self) -> WorkTarget:
        piece: Piece = PieceAt(BoardString(self.__target.fen()), FromSquare(self.__target.san())).value()
        if piece.symbol() == ".":
            raise RuntimeError(EmptyFromSquare(*(self.__target.value())).value())
        if piece.color() != self.__target.fen().split(" ")[1]:
            raise RuntimeError(OppositeFromSquare(*(self.__target.value())).value())

        return self.__target


class ToSquarePieceValidWorkTarget:
    __slots__ = ["__target"]

    __target: WorkTarget

    def __init__(self, target: WorkTarget):
        self.__target = target

    def value(self) -> WorkTarget:
        piece: Piece = PieceAt(BoardString(self.__target.fen()), ToSquare(self.__target.san())).value()
        if piece.symbol() != "." and piece.color() == self.__target.fen().split(" ")[1]:
            raise RuntimeError(FullToSquare(*(self.__target.value())).value())

        return self.__target


class LegalMoveWorkTarget:
    __slots__ = ["__target"]

    __target: WorkTarget

    def __init__(self, target: WorkTarget):
        self.__target = target

    def value(self) -> WorkTarget:
        if self.__target.san() not in LegalSANs(self.__target.fen()).value():
            raise RuntimeError(InvalidPieceMove(*(self.__target.value())).value())

        return self.__target


class ValidWorkTarget:
    __slots__ = ["__target"]

    __target: WorkTarget

    def __init__(self, target: WorkTarget):
        self.__target = target

    def value(self) -> WorkTarget:
        return (
            CastlableWorkTarget(self.__target).value()
            if self.__target.san() == MICRO_CASTLING_SAN
            else (
                Mappable(FromSquarePieceValidWorkTarget(self.__target).value())
                .mapped(lambda x: ToSquarePieceValidWorkTarget(x).value())
                .mapped(lambda x: LegalMoveWorkTarget(x).value())
                .value()
            )
        )
