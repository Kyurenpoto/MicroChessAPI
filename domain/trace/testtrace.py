# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import Optional

from ..microchess import MicroBoard, CreatedMicroBoard, MicroBoardStatus, MICRO_STARTING_FEN
from ..dto import testdto

class ChessSingleTrace(metaclass=ABCMeta):
    @abstractmethod
    def move(self, action: testdto.Action) -> testdto.ActionResult:
        pass

    @abstractmethod
    def reset(self, state: testdto.State) -> bool:
        pass

class Fake(ChessSingleTrace):
    def move(self, action: testdto.Action) -> testdto.ActionResult:
        return testdto.ActionResult(
            fen=MICRO_STARTING_FEN,
            status=MicroBoardStatus.NONE, 
            next_move_list=[])

    def reset(self, state: testdto.State) -> bool:
        return True

class ChessTestTrace(ChessSingleTrace):
    __slots__ = ["__board"]
    
    __board: MicroBoard

    def __init__(self):
        self.__board = MicroBoard()

    def move(self, action: testdto.Action) -> testdto.ActionResult:
        return testdto.ActionResult(
            fen=MICRO_STARTING_FEN,
            status=MicroBoardStatus.NONE, 
            next_move_list=[])

    def reset(self, state: testdto.State) -> bool:
        created: Optional[MicroBoard] = CreatedMicroBoard(state.fen).value()
        if created is None:
            return False

        self.__board = created

        return True
