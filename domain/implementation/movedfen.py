# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from infra.rawmovedfen import RawMovedFEN

from .basictype import FEN, SAN
from .mappable import Mappable
from .mirroredboardpart import MirroredBoardPart
from .splitablefen import CastlingPart, ColorPart, FullmovePart, ReplacableSplitedFEN


class NormalMovedFEN(FEN):
    @classmethod
    def from_FEN_SAN(cls, fen: FEN, san: SAN) -> NormalMovedFEN:
        return NormalMovedFEN(RawMovedFEN.from_FEN_SAN(fen, san))


class WhiteFullMoveCorrectedFEN(FEN):
    @classmethod
    def from_trace_FEN(cls, fen: FEN, next_fen: FEN) -> WhiteFullMoveCorrectedFEN:
        return WhiteFullMoveCorrectedFEN(
            ReplacableSplitedFEN.from_FEN(next_fen).replace_fullmove(FullmovePart.from_FEN(fen)).join_parts()
        )


class MirroredCastlingPart(CastlingPart):
    @classmethod
    def from_FEN(cls, fen: FEN) -> MirroredCastlingPart:
        return MirroredCastlingPart({"Kk": "Kk", "K": "k", "k": "K", "-": "-"}[CastlingPart.from_FEN(fen)])


class MirroredMicroFEN(FEN):
    @classmethod
    def from_FEN(cls, fen: FEN) -> MirroredMicroFEN:
        return MirroredMicroFEN(
            ReplacableSplitedFEN.from_FEN(fen)
            .replace_board_color_castling(
                MirroredBoardPart.from_FEN(fen),
                ColorPart.from_FEN(fen).mirror(),
                MirroredCastlingPart.from_FEN(fen),
            )
            .join_parts()
        )


class WhiteCastledFEN(FEN):
    @classmethod
    def from_FEN(cls, fen: FEN) -> WhiteCastledFEN:
        return WhiteCastledFEN(
            Mappable(MirroredMicroFEN.from_FEN(fen))
            .mapped(lambda x: NormalMovedFEN.from_FEN_SAN(x, SAN.castling()))
            .mapped(lambda x: MirroredMicroFEN.from_FEN(x))
            .mapped(lambda x: WhiteFullMoveCorrectedFEN.from_trace_FEN(fen, x))
            .value()
        )


class MovedFEN(FEN):
    @classmethod
    def from_FEN_SAN(cls, fen: FEN, san: SAN) -> MovedFEN:
        return MovedFEN(
            WhiteCastledFEN.from_FEN(fen)
            if san == SAN.castling() and ColorPart.from_FEN(fen) == "w"
            else NormalMovedFEN.from_FEN_SAN(fen, san)
        )
