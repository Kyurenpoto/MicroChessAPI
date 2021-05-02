# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import Optional

from domain.microchess import MicroBoard, CreatedMicroBoard, MicroBoardStatus, MICRO_STARTING_FEN
from domain.dto.testdto import Action, ActionResult, State

class ChessSingleTrace(metaclass=ABCMeta):
    @abstractmethod
    def move(self, action: Action) -> ActionResult:
        pass

    @abstractmethod
    def reset(self, state: State) -> bool:
        pass

class Fake(ChessSingleTrace):
    def move(self, action: Action) -> ActionResult:
        return ActionResult(
            fen=MICRO_STARTING_FEN,
            status=MicroBoardStatus.NONE, 
            next_move_list=[])

    def reset(self, state: State) -> bool:
        return True

class ChessTestTrace(ChessSingleTrace):
    __slots__ = ["__board"]
    
    __board: MicroBoard

    def __init__(self, board: MicroBoard = MicroBoard()):
        self.__board = board

    def __eq__(self, other) -> bool:
        return self.__board.fen() == other.__board.fen()

    def move(self, action: Action) -> ActionResult:
        return ActionResult(
            fen=MICRO_STARTING_FEN,
            status=MicroBoardStatus.NONE, 
            next_move_list=[])

    def reset(self, state: State) -> bool:
        created: Optional[MicroBoard] = CreatedMicroBoard(state.fen).value()
        if created is None:
            return False

        self.__board = created

        return True