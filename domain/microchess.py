# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations
from enum import Enum
from typing import Optional, Final

from infra.rawmovedfen import RawMovedFen
from .implementation.boardstring import FEN
from .implementation.microfen import ValidMicroFen, MirroredMicroFen
from .implementation.microsan import ValidMicroSAN, SAN, MICRO_CASTLING_SAN

MICRO_STARTING_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")
class MicroMove:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN = MICRO_CASTLING_SAN):
        self.__san = san

    def san(self) -> SAN:
        return self.__san

class CreatedMicroMove:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: str):
        self.__san = SAN(san)

    def value(self) -> MicroMove:
        san: Optional[SAN] = ValidMicroSAN(self.__san).value()
        if san is None:
            raise RuntimeError("Invalid SAN")

        return MicroMove(san)

class MicroBoardStatus(Enum):
    NONE = 0
    CHECKMATE = 1
    STALEMATE = 2

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
        fen: Optional[FEN] = ValidMicroFen(self.__fen).value()
        if fen is None:
            raise RuntimeError("Invalid FEN")
        
        return MicroBoard(fen)

class MovedMicroBoard:
    __slots__ = ["__fen", "__san"]

    __fen: FEN
    __san: SAN

    def __init__(self, fen: str, san: str):
        self.__fen = FEN(fen)
        self.__san = SAN(san)

    def value(self) -> MicroBoard:
        board: MicroBoard = CreatedMicroBoard(self.__fen).value()
        move: MicroMove = CreatedMicroMove(self.__san).value()

        if move.san() == MICRO_CASTLING_SAN:
            mirrored: FEN = MirroredMicroFen(board.fen()).value()
            moved: FEN = FEN(str(RawMovedFen(mirrored, move.san())))

            return MicroBoard(MirroredMicroFen(moved).value())
        else:
            return MicroBoard(FEN(str(RawMovedFen(board.fen(), move.san()))))
