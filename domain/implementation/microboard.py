# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, Optional

from infra.rawmovedfen import RawMovedFen

from .boardstring import FEN
from .mappable import Mappable
from .microfen import MirroredMicroFEN, ValidMicroFEN
from .micromove import CreatedMicroMove, MicroMove
from .microsan import MICRO_CASTLING_SAN, SAN

MICRO_STARTING_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")
MICRO_FIRST_MOVE_FEN: Final[FEN] = FEN("4knbr/4p3/7P/8/4RBNK/8/8/8 b Kk - 0 1")
MICRO_CHECKMATE_FEN: Final[FEN] = FEN("4k3/6B1/4R1K1/8/8/8/8/8 b Kk - 0 1")
MICRO_STALEMATE_FEN: Final[FEN] = FEN("4k3/6B1/5PK1/8/8/8/8/8 b Kk - 0 1")
MICRO_BLACK_CASTLABLE_FEN: Final[FEN] = FEN("4k2r/4p3/8/7P/4RBNK/8/8/8 b Kk - 0 1")
MICRO_WHITE_CASTLABLE_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/4R2K/8/8/8 w Kk - 0 1")


class MicroBoard:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN = MICRO_STARTING_FEN):
        self.__fen = fen

    def fen(self) -> FEN:
        return self.__fen


class CreatedMicroBoard:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: str):
        self.__fen = FEN(fen)

    def value(self) -> MicroBoard:
        fen: Optional[FEN] = ValidMicroFEN(self.__fen).value()
        if fen is None:
            raise RuntimeError("Invalid FEN")

        return MicroBoard(fen)


class NormalMovedMicroFEN:
    __slots__ = ["__fen", "__san"]

    __fen: FEN
    __san: SAN

    def __init__(self, fen: FEN, san: SAN):
        self.__fen = fen
        self.__san = san

    def value(self) -> FEN:
        return FEN(str(RawMovedFen(self.__fen, self.__san)))


class CastleMovedMicroFEN:
    __slots__ = ["__fen", "__san"]

    __fen: FEN
    __san: SAN

    def __init__(self, fen: FEN, san: SAN):
        self.__fen = fen
        self.__san = san

    def value(self) -> FEN:
        return (
            Mappable(MirroredMicroFEN(self.__fen).value())
            .mapped(lambda x: NormalMovedMicroFEN(x, self.__san).value())
            .mapped(lambda x: MirroredMicroFEN(x).value())
            .value()
        )


class MovedMicroBoard:
    __slots__ = ["__fen", "__san"]

    __fen: FEN
    __san: SAN

    def __init__(self, fen: FEN, san: SAN):
        self.__fen = fen
        self.__san = san

    def value(self) -> MicroBoard:
        fen: FEN = CreatedMicroBoard(self.__fen).value().fen()
        san: SAN = CreatedMicroMove(self.__san).value().san()

        return MicroBoard(
            CastleMovedMicroFEN(fen, san).value()
            if san == MICRO_CASTLING_SAN
            else NormalMovedMicroFEN(fen, san).value()
        )
