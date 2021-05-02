# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import List

from domain.microchess import MicroBoard, CreatedMicroBoard, MICRO_STARTING_FEN
from domain.dto.traindto import Action, ActionResult, State

class ChessMultiTrace(metaclass=ABCMeta):
    @abstractmethod
    def move(self, action: Action) -> ActionResult:
        pass

    @abstractmethod
    def reset(self, state: State) -> bool:
        pass

class Fake(ChessMultiTrace):
    def move(self, action: Action) -> ActionResult:
        return ActionResult(
            fens=[MICRO_STARTING_FEN],
            statuses=[],
            next_move_lists=[])

    def reset(self, state: State) -> bool:
        return True

class ChessTrainTrace(ChessMultiTrace):
    __slots__ = ["__boards"]
    
    __boards: List[MicroBoard]

    def __init__(self, boards: List[MicroBoard] = []):
        self.__boards = boards

    def __eq__(self, other) -> bool:
        size: int = len(self.__boards)
        if size != len(other.__boards):
            return False
        
        for i in range(0, size):
            if self.__boards[i].fen() != other.__boards[i].fen():
                return False
        
        return True

    def move(self, action: Action) -> ActionResult:
        return ActionResult(
            fens=[MICRO_STARTING_FEN],
            statuses=[],
            next_move_lists=[])

    def reset(self, state: State) -> bool:
        creates: List[MicroBoard] = []
        for fen in state.fens:
            created = CreatedMicroBoard(fen).value()
            if created is None:
                return False
            
            creates.append(created)

        self.__boards = creates[:]

        return True
