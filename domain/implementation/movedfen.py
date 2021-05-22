# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from infra.rawmovedfen import RawMovedFEN

from .basictype import FEN, SAN
from .mappable import Mappable
from .microfen import MirroredMicroFEN


class NormalMovedFEN(FEN):
    @classmethod
    def from_FEN_SAN(cls, fen: FEN, san: SAN) -> NormalMovedFEN:
        return NormalMovedFEN(RawMovedFEN.from_FEN_SAN(fen, san))


class WhiteFullMoveCorrectedFEN(FEN):
    @classmethod
    def from_trace_FEN(cls, fen: FEN, next_fen: FEN) -> WhiteFullMoveCorrectedFEN:
        return WhiteFullMoveCorrectedFEN(" ".join(next_fen.split(" ")[:-1] + [fen.split(" ")[-1]]))


class WhiteCastledFEN(FEN):
    @classmethod
    def from_FEN(cls, fen: FEN) -> WhiteCastledFEN:
        return WhiteCastledFEN(
            Mappable(MirroredMicroFEN(fen).value())
            .mapped(lambda x: NormalMovedFEN.from_FEN_SAN(x, SAN.castling()))
            .mapped(lambda x: MirroredMicroFEN(x).value())
            .mapped(lambda x: WhiteFullMoveCorrectedFEN.from_trace_FEN(fen, x))
            .value()
        )


class MovedFEN(FEN):
    @classmethod
    def from_FEN_SAN(cls, fen: FEN, san: SAN) -> MovedFEN:
        return MovedFEN(
            WhiteCastledFEN.from_FEN(fen)
            if san == SAN.castling() and fen.split(" ")[1] == "w"
            else NormalMovedFEN.from_FEN_SAN(fen, san)
        )
