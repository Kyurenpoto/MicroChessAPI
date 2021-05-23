# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from domain.error.microfenerror import (
    InvalidCastlingPart,
    InvalidEnpassantPart,
    InvalidFullmovePart,
    InvalidHalfmovePart,
    InvalidStructure,
    InvalidTurnPart,
)

from .boardstring import BoardString, ValidMicroBoardString
from .mappable import Mappable
from .microfen import MicroFEN
from .splitablefen import (
    BoardPart,
    CastlingPart,
    ColorPart,
    EnpassantPart,
    FullmovePart,
    HalfmovePart,
    RawFullmovePart,
    RawHalfmovePart,
    SplitedFEN,
)
from .validboardpart import ValidBoardPart


class StructureValidMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, microfen: MicroFEN) -> StructureValidMicroFEN:
        if len(SplitedFEN.from_FEN(microfen.fen)) != 6:
            raise RuntimeError(InvalidStructure.from_index_with_FENs(microfen.index, microfen.fens))

        return StructureValidMicroFEN(microfen.index, microfen.fens, microfen.fen)


class BoardPartValidMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, microfen: MicroFEN) -> BoardPartValidMicroFEN:
        valid: MicroFEN = (
            Mappable(ValidBoardPart.from_raw(BoardPart.from_MicroFEN(microfen)).fen)
            .mapped(lambda x: ValidMicroBoardString.from_boardstring(BoardString.from_MicroFEN(x)).microfen)
            .value()
        )

        return BoardPartValidMicroFEN(valid.index, valid.fens, valid.fen)


class TurnPartValidMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, microfen: MicroFEN) -> TurnPartValidMicroFEN:
        if ColorPart.from_FEN(microfen.fen) not in ["w", "b"]:
            raise RuntimeError(InvalidTurnPart.from_index_with_FENs(microfen.index, microfen.fens))

        return TurnPartValidMicroFEN(microfen.index, microfen.fens, microfen.fen)


class CastlingPartValidMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, microfen: MicroFEN) -> CastlingPartValidMicroFEN:
        if CastlingPart.from_FEN(microfen.fen) not in ["Kk", "K", "k", "-"]:
            raise RuntimeError(InvalidCastlingPart.from_index_with_FENs(microfen.index, microfen.fens))

        return CastlingPartValidMicroFEN(microfen.index, microfen.fens, microfen.fen)


class EnpassantPartValidMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, microfen: MicroFEN) -> EnpassantPartValidMicroFEN:
        if EnpassantPart.from_FEN(microfen.fen) != "-":
            raise RuntimeError(InvalidEnpassantPart.from_index_with_FENs(microfen.index, microfen.fens))

        return EnpassantPartValidMicroFEN(microfen.index, microfen.fens, microfen.fen)


class HalfmovePartValidMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, microfen: MicroFEN) -> HalfmovePartValidMicroFEN:
        raw: RawHalfmovePart = RawHalfmovePart.from_FEN(microfen.fen)
        if not (raw.isdecimal() and 0 <= HalfmovePart.from_raw(raw) <= 50):
            raise RuntimeError(InvalidHalfmovePart.from_index_with_FENs(microfen.index, microfen.fens))

        return HalfmovePartValidMicroFEN(microfen.index, microfen.fens, microfen.fen)


class FullmovePartValidMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, microfen: MicroFEN) -> FullmovePartValidMicroFEN:
        raw: RawFullmovePart = RawFullmovePart.from_FEN(microfen.fen)
        if not (raw.isdecimal() and 1 <= FullmovePart.from_raw(raw) <= 80):
            raise RuntimeError(InvalidFullmovePart.from_index_with_FENs(microfen.index, microfen.fens))

        return FullmovePartValidMicroFEN(microfen.index, microfen.fens, microfen.fen)


class ValidMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, microfen: MicroFEN) -> ValidMicroFEN:
        valid: MicroFEN = (
            Mappable(StructureValidMicroFEN.from_MicroFEN(microfen))
            .mapped(lambda x: BoardPartValidMicroFEN.from_MicroFEN(x))
            .mapped(lambda x: TurnPartValidMicroFEN.from_MicroFEN(x))
            .mapped(lambda x: CastlingPartValidMicroFEN.from_MicroFEN(x))
            .mapped(lambda x: EnpassantPartValidMicroFEN.from_MicroFEN(x))
            .mapped(lambda x: HalfmovePartValidMicroFEN.from_MicroFEN(x))
            .mapped(lambda x: FullmovePartValidMicroFEN.from_MicroFEN(x))
            .value()
        )

        return ValidMicroFEN(valid.index, valid.fens, valid.fen)
