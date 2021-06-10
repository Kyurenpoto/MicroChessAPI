# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from src.domain.implementation.basictype import FEN, SAN
from src.domain.implementation.mirroredboardpart import MirroredBoardPart
from src.infra.splitablefen import CastlingPart, ColorPart, FullmovePart, ReplacableSplitedFEN
from src.infra.rawmovedfen import RawMovedFEN


class MirroredCastlingPart(CastlingPart):
    @classmethod
    def from_FEN(cls, fen: FEN) -> MirroredCastlingPart:
        return MirroredCastlingPart({"Kk": "Kk", "K": "k", "k": "K", "-": "-"}[CastlingPart.from_FEN(fen)])


class MovableFEN(FEN):
    def moved(self, san: SAN) -> MovableFEN:
        return MovableFEN(
            self.white_castled()
            if san == SAN.castling() and ColorPart.from_FEN(self) == "w"
            else self.normal_moved(san)
        )

    def white_castled(self) -> MovableFEN:
        return self.mirrored().normal_moved(SAN.castling()).mirrored().white_fullmove_corrected(self)

    def normal_moved(self, san: SAN) -> MovableFEN:
        return MovableFEN(RawMovedFEN.from_FEN_SAN(self, san))

    def mirrored(self) -> MovableFEN:
        return MovableFEN(
            ReplacableSplitedFEN.from_FEN(self)
            .replace_board_color_castling(
                MirroredBoardPart.from_FEN(self),
                ColorPart.from_FEN(self).mirror(),
                MirroredCastlingPart.from_FEN(self),
            )
            .join_parts()
        )

    def white_fullmove_corrected(self, prev_fen: FEN) -> MovableFEN:
        return MovableFEN(
            ReplacableSplitedFEN.from_FEN(self).replace_fullmove(FullmovePart.from_FEN(prev_fen)).join_parts()
        )
