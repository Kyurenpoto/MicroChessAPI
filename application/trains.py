# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import Dict

from domain.dto.trains import Action, ActionResult, State
from domain.trace import TrainsTrace

class TrainsBase(metaclass=ABCMeta):
    @abstractmethod
    async def move(self, action: Action) -> ActionResult:
        pass

    @abstractmethod
    async def reset(self, state: State) -> Dict[str, bool]:
        pass

class Fake(TrainsBase):
    async def move(self, action: Action) -> ActionResult:
        return ActionResult(fens=[], statuses=[], next_move_lists=[])

    async def reset(self, state: State) -> Dict[str, bool]:
        return {"success": True}

class Trains(TrainsBase):
    __slots__ = ["__trace"]

    __trace: TrainsTrace

    def __init__(self):
        self.__trace = TrainsTrace()

    async def move(self, action: Action) -> ActionResult:
        return self.__trace.move(action)

    async def reset(self, state: State) -> Dict[str, bool]:
        return {"success": self.__trace.reset(state)}
