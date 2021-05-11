# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, List

from infra.rawmovedfen import RawMovedFen

from .basictype import FEN, SAN
from .mappable import Mappable
from .microfen import MirroredMicroFEN, ValidMicroFEN
from .micromove import CreatedMicroMove
from .microsan import MICRO_CASTLING_SAN

MICRO_STARTING_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")
MICRO_FIRST_MOVE_FEN: Final[FEN] = FEN("4knbr/4p3/7P/8/4RBNK/8/8/8 b Kk - 0 1")
MICRO_CHECKMATE_FEN: Final[FEN] = FEN("4k3/6B1/4R1K1/8/8/8/8/8 b Kk - 0 1")
MICRO_STALEMATE_FEN: Final[FEN] = FEN("4k3/6B1/5PK1/8/8/8/8/8 b Kk - 0 1")
MICRO_BLACK_CASTLABLE_FEN: Final[FEN] = FEN("4k2r/4p3/8/7P/4RBNK/8/8/8 b Kk - 0 1")
MICRO_WHITE_CASTLABLE_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/4R2K/8/8/8 w Kk - 0 1")
MICRO_BLACK_CASTLED_FEN: Final[FEN] = FEN("5rk1/4p3/8/7P/4RBNK/8/8/8 w K - 1 2")
MICRO_WHITE_CASTLED_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/5KR1/8/8/8 b k - 1 1")
MICRO_ONLY_KING_FEN: Final[FEN] = FEN("4k3/8/8/8/7K/8/8/8 w - - 0 1")
MICRO_SWAP_KING_BISHOP_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/4RK1B/8/8/8 w Kk - 0 1")


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
        return MicroBoard(ValidMicroFEN(self.__fen).value())


class NormalMovedMicroFEN:
    __slots__ = ["__fen", "__san"]

    __fen: FEN
    __san: SAN

    def __init__(self, fen: FEN, san: SAN):
        self.__fen = fen
        self.__san = san

    def value(self) -> FEN:
        return FEN(str(RawMovedFen(self.__fen, self.__san)))


class WhiteFullMoveCorrectedMicroFEN:
    __slots__ = ["__origin", "__moved"]

    __origin: FEN
    __moved: FEN

    def __init__(self, origin: FEN, moved: FEN):
        self.__origin = origin
        self.__moved = moved

    def value(self) -> FEN:
        origin: List[str] = self.__origin.split(" ")
        moved: List[str] = self.__moved.split(" ")

        return FEN(" ".join(moved[:-1] + [origin[-1]]))


class WhiteCastledMicroFEN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> FEN:
        return (
            Mappable(MirroredMicroFEN(self.__fen).value())
            .mapped(lambda x: NormalMovedMicroFEN(x, MICRO_CASTLING_SAN).value())
            .mapped(lambda x: MirroredMicroFEN(x).value())
            .mapped(lambda x: WhiteFullMoveCorrectedMicroFEN(self.__fen, x).value())
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
        return MicroBoard(
            WhiteCastledMicroFEN(self.__fen).value()
            if self.__san == MICRO_CASTLING_SAN and self.__fen.split(" ")[1] == "w"
            else NormalMovedMicroFEN(self.__fen, self.__san).value()
        )
