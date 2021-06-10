# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from src.domain.error.microfenerror import (
    InvalidCastlingPart,
    InvalidEnpassantPart,
    InvalidFullmovePart,
    InvalidHalfmovePart,
    InvalidStructure,
    InvalidTurnPart,
)
from src.domain.implementation.microfen import MicroFEN
from src.infra.splitablefen import (
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
from src.domain.implementation.validboardpart import ValidBoardPart


class ValidMicroFEN(MicroFEN):
    @classmethod
    def from_MicroFEN(cls, microfen: MicroFEN) -> ValidMicroFEN:
        return ValidMicroFEN._make(
            ValidMicroFEN._make(microfen)
            .valid_structure()
            .valid_board_part()
            .valid_turn_part()
            .valid_castling_part()
            .valid_enpassant_part()
            .valid_halfmove_part()
            .valid_fullmove_part()
        )

    def valid_structure(self) -> ValidMicroFEN:
        if len(SplitedFEN.from_FEN(self.fen)) != 6:
            raise RuntimeError(InvalidStructure.from_index_with_FENs(self.index, self.fens))

        return self

    def valid_board_part(self) -> ValidMicroFEN:
        return ValidMicroFEN._make(ValidBoardPart.from_raw(BoardPart.from_MicroFEN(self)).fen)

    def valid_turn_part(self) -> ValidMicroFEN:
        if ColorPart.from_FEN(self.fen) not in ["w", "b"]:
            raise RuntimeError(InvalidTurnPart.from_index_with_FENs(self.index, self.fens))

        return self

    def valid_castling_part(self) -> ValidMicroFEN:
        if CastlingPart.from_FEN(self.fen) not in ["Kk", "K", "k", "-"]:
            raise RuntimeError(InvalidCastlingPart.from_index_with_FENs(self.index, self.fens))

        return self

    def valid_enpassant_part(self) -> ValidMicroFEN:
        if EnpassantPart.from_FEN(self.fen) != "-":
            raise RuntimeError(InvalidEnpassantPart.from_index_with_FENs(self.index, self.fens))

        return self

    def valid_halfmove_part(self) -> ValidMicroFEN:
        raw: RawHalfmovePart = RawHalfmovePart.from_FEN(self.fen)
        if not (raw.isdecimal() and 0 <= HalfmovePart.from_raw(raw) <= 50):
            raise RuntimeError(InvalidHalfmovePart.from_index_with_FENs(self.index, self.fens))

        return self

    def valid_fullmove_part(self) -> ValidMicroFEN:
        raw: RawFullmovePart = RawFullmovePart.from_FEN(self.fen)
        if not (raw.isdecimal() and 1 <= FullmovePart.from_raw(raw) <= 80):
            raise RuntimeError(InvalidFullmovePart.from_index_with_FENs(self.index, self.fens))

        return self
