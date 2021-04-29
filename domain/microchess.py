# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from enum import Enum

import chess

class MicroFen:
    __slots__ = ["__fen"]

    def __init__(self, fen: str):
        self.__fen = fen

    def __str__(self):
        return self.__fen

class MicroMove:
    def __init__(self, move: str):
        pass

class MicroBoardStatus(Enum):
    NONE = 0
    CHECKMATE = 1
    STALEMATE = 2

class MicroBoardBase(metaclass=ABCMeta):
    @abstractmethod
    def fen(self) -> MicroFen:
        pass

    @abstractmethod
    def move(self, move: MicroMove):
        pass

class MicroBoard(MicroBoardBase):
    def __init__(self, fen: MicroFen):
        pass

    def __init__(self, fen: str):
        self.__init__(MicroFen(fen))

    def fen(self) -> MicroFen:
        pass

    def move(self, move: MicroMove) -> MicroBoardBase:
        pass
