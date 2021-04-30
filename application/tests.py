# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import Dict

from domain.microchess import MicroBoardStatus, MICRO_STARTING_FEN
from domain.dto.tests import Action, ActionResult, State
from domain.trace import TestsTrace

class TestsBase(metaclass=ABCMeta):
    @abstractmethod
    async def move(self, action: Action) -> ActionResult:
        pass

    @abstractmethod
    async def reset(self, state: State) -> Dict[str, bool]:
        pass

class Fake(TestsBase):
    async def move(self, action: Action) -> ActionResult:
        return ActionResult(
            fen=MICRO_STARTING_FEN,
            status=MicroBoardStatus.NONE,
            next_move_list=[])

    async def reset(self, state: State) -> Dict[str, bool]:
        return {"success": True}

class Tests(TestsBase):
    __slots__ = ["__trace"]

    __trace: TestsTrace

    def __init__(self):
        self.__trace = TestsTrace()

    async def move(self, action: Action) -> ActionResult:
        return self.__trace.move(action)

    async def reset(self, state: State) -> Dict[str, bool]:
        return {"success": self.__trace.reset(state)}
