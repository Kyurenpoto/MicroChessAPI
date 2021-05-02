# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import Dict

from domain.microchess import MICRO_STARTING_FEN
from domain.dto.trains import Action, ActionResult, State
from domain.trace import TrainChessTrace

class MultiChessEnvironment(metaclass=ABCMeta):
    @abstractmethod
    async def move(self, action: Action) -> ActionResult:
        pass

    @abstractmethod
    async def reset(self, state: State) -> Dict[str, bool]:
        pass

class Fake(MultiChessEnvironment):
    async def move(self, action: Action) -> ActionResult:
        return ActionResult(
            fens=[MICRO_STARTING_FEN],
            statuses=[],
            next_move_lists=[])

    async def reset(self, state: State) -> Dict[str, bool]:
        return {"success": True}

class TrainChessEnvironment(MultiChessEnvironment):
    __slots__ = ["__trace"]

    __trace: TrainChessTrace

    def __init__(self):
        self.__trace = TrainChessTrace()

    async def move(self, action: Action) -> ActionResult:
        return self.__trace.move(action)

    async def reset(self, state: State) -> Dict[str, bool]:
        return {"success": self.__trace.reset(state)}
