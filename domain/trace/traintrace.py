# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import List

from ..microchess import MicroBoard, CreatedMicroBoard, MICRO_STARTING_FEN
from ..dto import traindto

class ChessMultiTrace(metaclass=ABCMeta):
    @abstractmethod
    def move(self, action: traindto.Action) -> traindto.ActionResult:
        pass

    @abstractmethod
    def reset(self, state: traindto.State) -> bool:
        pass

class Fake(ChessMultiTrace):
    def move(self, action: traindto.Action) -> traindto.ActionResult:
        return traindto.ActionResult(
            fens=[MICRO_STARTING_FEN],
            statuses=[],
            next_move_lists=[])

    def reset(self, state: traindto.State) -> bool:
        return True

class ChessTrainTrace(ChessMultiTrace):
    __slots__ = ["__boards"]
    
    __boards: List[MicroBoard]

    def __init__(self):
        self.__boards = []

    def move(self, action: traindto.Action) -> traindto.ActionResult:
        return traindto.ActionResult(
            fens=[MICRO_STARTING_FEN],
            statuses=[],
            next_move_lists=[])

    def reset(self, state: traindto.State) -> bool:
        creates: List[MicroBoard] = []
        for fen in state.fens:
            created = CreatedMicroBoard(fen).value()
            if created is None:
                return False
            
            creates.append(created)

        self.__boards = creates[:]

        return True
