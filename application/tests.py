# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import Dict

from domain.dto.tests import Action, ActionResult, State
from domain.microchess import MicroBoardStatus

class TestsBase(metaclass=ABCMeta):
    @abstractmethod
    async def move(self, action: Action) -> ActionResult:
        pass

    @abstractmethod
    async def reset(self, state: State) -> Dict[str, bool]:
        pass

class Fake(TestsBase):
    async def move(self, action: Action) -> ActionResult:
        return ActionResult(fen="", status=MicroBoardStatus.NONE, next_move_list=[])

    async def reset(self, state: State) -> Dict[str, bool]:
        return {"success": True}

class Tests(TestsBase):
    async def move(self, action: Action) -> ActionResult:
        return ActionResult(fen="", status=MicroBoardStatus.NONE, next_move_list=[])

    async def reset(self, state: State) -> Dict[str, bool]:
        return {"success": True}
