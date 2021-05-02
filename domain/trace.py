# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import List, Optional

from .microchess import MicroBoard, CreatedMicroBoard, MicroBoardStatus, MICRO_STARTING_FEN
from .dto import tests, trains

class SingleChessTrace:
    @abstractmethod
    def move(self, action: tests.Action) -> tests.ActionResult:
        pass

    @abstractmethod
    def reset(self, state: tests.State) -> bool:
        pass

class TestChessTrace(SingleChessTrace):
    __slots__ = ["__board"]
    
    __board: MicroBoard

    def __init__(self):
        self.__board = MicroBoard()

    def move(self, action: tests.Action) -> tests.ActionResult:
        return tests.ActionResult(
            fen=MICRO_STARTING_FEN,
            status=MicroBoardStatus.NONE, 
            next_move_list=[])

    def reset(self, state: tests.State) -> bool:
        created: Optional[MicroBoard] = CreatedMicroBoard(state.fen).value()
        if created is None:
            return False

        self.__board = created

        return True

class MultiChessTrace:
    @abstractmethod
    def move(self, action: trains.Action) -> trains.ActionResult:
        pass

    @abstractmethod
    def reset(self, state: trains.State) -> bool:
        pass

class TrainChessTrace(MultiChessTrace):
    __slots__ = ["__boards"]
    
    __boards: List[MicroBoard]

    def __init__(self):
        self.__boards = []

    def move(self, action: trains.Action) -> trains.ActionResult:
        return trains.ActionResult(
            fens=[MICRO_STARTING_FEN],
            statuses=[],
            next_move_lists=[])

    def reset(self, state: trains.State) -> bool:
        creates: List[MicroBoard] = []
        for fen in state.fens:
            created = CreatedMicroBoard(fen).value()
            if created is None:
                return False
            
            creates.append(created)

        self.__boards = creates[:]

        return True
