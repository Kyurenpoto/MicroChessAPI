# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import Optional

from domain.microchess import MicroBoard, CreatedMicroBoard, MicroBoardStatus, MICRO_STARTING_FEN
from domain.dto.testdto import Action, ActionResult, State

from test.constant import MICRO_FIRST_MOVE_FEN, MICRO_FIRST_NEXT_MOVE_LIST

class ChessSingleTrace(metaclass=ABCMeta):
    @abstractmethod
    def move(self, action: Action) -> ActionResult:
        pass

    @abstractmethod
    def reset(self, state: State) -> None:
        pass

class Fake(ChessSingleTrace):
    def move(self, action: Action) -> ActionResult:
        return ActionResult(
            fen=MICRO_FIRST_MOVE_FEN,
            status=MicroBoardStatus.NONE, 
            next_move_list=MICRO_FIRST_NEXT_MOVE_LIST)

    def reset(self, state: State) -> None:
        pass

class ChessTestTrace(ChessSingleTrace):
    __slots__ = ["__board"]
    
    __board: MicroBoard

    def __init__(self, board: MicroBoard = MicroBoard()):
        self.__board = board

    def __eq__(self, other) -> bool:
        return self.__board.fen() == other.__board.fen()

    def move(self, action: Action) -> ActionResult:
        return ActionResult(
            fen=MICRO_FIRST_MOVE_FEN,
            status=MicroBoardStatus.NONE, 
            next_move_list=MICRO_FIRST_NEXT_MOVE_LIST)

    def reset(self, state: State) -> None:
        created: Optional[MicroBoard] = CreatedMicroBoard(state.fen).value()
        if created is None:
            raise RuntimeError("Invalid FEN")

        self.__board = created
