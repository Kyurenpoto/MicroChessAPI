# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations
from enum import Enum
from typing import Optional, Final, NewType

from .implementation.extendtype import Nullable
from .implementation.boardstring import FEN
from .implementation.microfen import ValidMicroFen

MICRO_STARTING_FEN: Final[FEN] = FEN("4kbnr/4p3/8/7P/4RNBK/8/8/8 w Kk - 0 1")

SAN = NewType('SAN', str)

MICRO_CASTLING_SAN: Final[SAN] = SAN("O-O")

class ValidMicroSAN:
        pass

class MicroBoardStatus(Enum):
    NONE = 0
    CHECKMATE = 1
    STALEMATE = 2

class MicroBoard:
    __slots__ = ["__fen", "__reversed_fen"]

    __fen: FEN
    __reversed_fen: FEN

    def __init__(self, fen: FEN = MICRO_STARTING_FEN):
        self.__fen = fen

    def fen(self) -> FEN:
        return self.__fen

    def move(self, move: MicroMove) -> MicroBoard:
        return MicroBoard()

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
