# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import NamedTuple

from infra.rawmovedfen import RawMovedFen

from .basictype import FEN, SAN
from .mappable import Mappable
from .microfen import MirroredMicroFEN
from .validmicrosan import MICRO_CASTLING_SAN


class NormalMovedFEN(NamedTuple):
    fen: FEN
    san: SAN

    def value(self) -> FEN:
        return FEN(str(RawMovedFen(self.fen, self.san)))


class WhiteFullMoveCorrectedFEN(NamedTuple):
    origin: FEN
    moved: FEN

    def value(self) -> FEN:
        return FEN(" ".join(self.moved.split(" ")[:-1] + [self.origin.split(" ")[-1]]))


class WhiteCastledFEN(NamedTuple):
    fen: FEN

    def value(self) -> FEN:
        return (
            Mappable(MirroredMicroFEN(self.fen).value())
            .mapped(lambda x: NormalMovedFEN(x, MICRO_CASTLING_SAN).value())
            .mapped(lambda x: MirroredMicroFEN(x).value())
            .mapped(lambda x: WhiteFullMoveCorrectedFEN(self.fen, x).value())
            .value()
        )


class MovedFEN(NamedTuple):
    fen: FEN
    san: SAN

    def value(self) -> FEN:
        return (
            WhiteCastledFEN(self.fen).value()
            if self.san == MICRO_CASTLING_SAN and self.fen.split(" ")[1] == "w"
            else NormalMovedFEN(self.fen, self.san).value()
        )
