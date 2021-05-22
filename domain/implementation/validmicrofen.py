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

from .boardstring import BoardString, valid_micro_board_string
from .mappable import Mappable
from .microfen import MicroFEN


class ValidStructedMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, fen: MicroFEN) -> ValidStructedMicroFEN:
        if len(fen.fen().split(" ")) != 6:
            raise RuntimeError(InvalidStructure.from_index_with_FENs(fen.index(), fen.fens()))

        return ValidStructedMicroFEN(fen.index(), fen.fens())


class ValidBoardPartMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, fen: MicroFEN) -> ValidBoardPartMicroFEN:
        valid: MicroFEN = valid_micro_board_string(BoardString(fen)).fen()
        return ValidBoardPartMicroFEN(valid.index(), valid.fens())


class ValidTurnPartMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, fen: MicroFEN) -> ValidTurnPartMicroFEN:
        if fen.fen().split(" ")[1] not in ["w", "b"]:
            raise RuntimeError(InvalidTurnPart.from_index_with_FENs(fen.index(), fen.fens()))

        return ValidTurnPartMicroFEN(fen.index(), fen.fens())


class ValidCastlingPartMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, fen: MicroFEN) -> ValidCastlingPartMicroFEN:
        if fen.fen().split(" ")[2] not in ["Kk", "K", "k", "-"]:
            raise RuntimeError(InvalidCastlingPart.from_index_with_FENs(fen.index(), fen.fens()))

        return ValidCastlingPartMicroFEN(fen.index(), fen.fens())


class ValidEnpassantPartMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, fen: MicroFEN) -> ValidEnpassantPartMicroFEN:
        if fen.fen().split(" ")[3] != "-":
            raise RuntimeError(InvalidEnpassantPart.from_index_with_FENs(fen.index(), fen.fens()))

        return ValidEnpassantPartMicroFEN(fen.index(), fen.fens())


class ValidHalfmovePartMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, fen: MicroFEN) -> ValidHalfmovePartMicroFEN:
        halfmove: str = fen.fen().split(" ")[4]
        if not (halfmove.isdigit() and 0 <= int(halfmove) <= 50):
            raise RuntimeError(InvalidHalfmovePart.from_index_with_FENs(fen.index(), fen.fens()))

        return ValidHalfmovePartMicroFEN(fen.index(), fen.fens())


class ValidFullmovePartMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, fen: MicroFEN) -> ValidFullmovePartMicroFEN:
        fullmove: str = fen.fen().split(" ")[5]
        if not (fullmove.isdigit() and 1 <= int(fullmove) <= 80):
            raise RuntimeError(InvalidFullmovePart.from_index_with_FENs(fen.index(), fen.fens()))

        return ValidFullmovePartMicroFEN(fen.index(), fen.fens())


class ValidMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, fen: MicroFEN) -> ValidMicroFEN:
        valid: MicroFEN = (
            Mappable(ValidStructedMicroFEN.from_MicroFEN(fen))
            .mapped(lambda x: ValidBoardPartMicroFEN.from_MicroFEN(x))
            .mapped(lambda x: ValidTurnPartMicroFEN.from_MicroFEN(x))
            .mapped(lambda x: ValidCastlingPartMicroFEN.from_MicroFEN(x))
            .mapped(lambda x: ValidEnpassantPartMicroFEN.from_MicroFEN(x))
            .mapped(lambda x: ValidHalfmovePartMicroFEN.from_MicroFEN(x))
            .mapped(lambda x: ValidFullmovePartMicroFEN.from_MicroFEN(x))
            .value()
        )

        return ValidMicroFEN(valid.index(), valid.fens())
