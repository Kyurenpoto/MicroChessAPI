# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from infra.rawmovedfen import RawMovedFen

from .basictype import FEN, SAN
from .mappable import Mappable
from .microfen import MirroredMicroFEN
from .validmicrosan import MICRO_CASTLING_SAN


class NormalMovedFEN:
    __slots__ = ["__fen", "__san"]

    __fen: FEN
    __san: SAN

    def __init__(self, fen: FEN, san: SAN):
        self.__fen = fen
        self.__san = san

    def value(self) -> FEN:
        return FEN(str(RawMovedFen(self.__fen, self.__san)))


class WhiteFullMoveCorrectedFEN:
    __slots__ = ["__origin", "__moved"]

    __origin: FEN
    __moved: FEN

    def __init__(self, origin: FEN, moved: FEN):
        self.__origin = origin
        self.__moved = moved

    def value(self) -> FEN:
        origin: list[str] = self.__origin.split(" ")
        moved: list[str] = self.__moved.split(" ")

        return FEN(" ".join(moved[:-1] + [origin[-1]]))


class WhiteCastledFEN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> FEN:
        return (
            Mappable(MirroredMicroFEN(self.__fen).value())
            .mapped(lambda x: NormalMovedFEN(x, MICRO_CASTLING_SAN).value())
            .mapped(lambda x: MirroredMicroFEN(x).value())
            .mapped(lambda x: WhiteFullMoveCorrectedFEN(self.__fen, x).value())
            .value()
        )


class MovedFEN:
    __slots__ = ["__fen", "__san"]

    __fen: FEN
    __san: SAN

    def __init__(self, fen: FEN, san: SAN):
        self.__fen = fen
        self.__san = san

    def value(self) -> FEN:
        return (
            WhiteCastledFEN(self.__fen).value()
            if self.__san == MICRO_CASTLING_SAN and self.__fen.split(" ")[1] == "w"
            else NormalMovedFEN(self.__fen, self.__san).value()
        )
