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
from .microfen import MicroFEN
from .microsan import MicroSAN, ValidMicroSAN
from .movedfen import MirroredMicroFEN
from .splitablefen import ColorPart
from .square import FromSquare, Square, ToSquare


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
            self.__fen = ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(self.__index, self.__fens))

        return self.__fen

    def microsan(self) -> MicroSAN:
        if self.__san is None:
            self.__san = ValidMicroSAN.from_MicroSAN(MicroSAN(self.__index, self.__sans))

        return self.__san

    def fen(self) -> FEN:
        return self.microfen().fen

    def san(self) -> SAN:
        return self.microsan().san()


class CastlableMoveTarget(NamedTuple):
    target: MoveTarget

    def value(self) -> MoveTarget:
        if SAN.castling() not in LegalSANs.from_FEN(
            self.target.fen()
            if ColorPart.from_FEN(self.target.fen()) == "b"
            else MirroredMicroFEN.from_FEN(self.target.fen())
        ):
            raise RuntimeError(CannotCastle.from_index_with_FENs_SANs(*(self.target.value())))

        return self.target


class Piece(str):
    @classmethod
    def from_board_with_square(cls, board: BoardString, square: Square):
        file_val: int = ord(square.file()) - ord("a")
        rank_val: int = ord(square.rank()) - ord("1")

        return Piece(board.board[file_val + ((7 - rank_val) * 8)])

    def color(self) -> str:
        return "w" if self.isupper() else "b"


class FromSquarePieceValidMoveTarget(NamedTuple):
    target: MoveTarget

    def value(self) -> MoveTarget:
        piece: Piece = Piece.from_board_with_square(
            BoardString.from_MicroFEN(self.target.microfen()), FromSquare.from_SAN(self.target.san())
        )
        if piece == ".":
            raise RuntimeError(EmptyFromSquare.from_index_with_FENs_SANs(*(self.target.value())))
        if piece.color() != ColorPart.from_FEN(self.target.fen()):
            raise RuntimeError(OppositeFromSquare.from_index_with_FENs_SANs(*(self.target.value())))

        return self.target


class ToSquarePieceValidMoveTarget(NamedTuple):
    target: MoveTarget

    def value(self) -> MoveTarget:
        piece: Piece = Piece.from_board_with_square(
            BoardString.from_MicroFEN(self.target.microfen()), ToSquare.from_SAN(self.target.san())
        )
        if piece != "." and piece.color() == ColorPart.from_FEN(self.target.fen()):
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
            if self.target.san() == SAN.castling()
            else (
                Mappable(FromSquarePieceValidMoveTarget(self.target).value())
                .mapped(lambda x: ToSquarePieceValidMoveTarget(x).value())
                .mapped(lambda x: LegalMoveMoveTarget(x).value())
                .value()
            )
        )
