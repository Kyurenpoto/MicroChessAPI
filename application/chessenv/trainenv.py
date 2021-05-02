# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

from domain.dto.traindto import Action, ActionResult, State
from domain.trace.traintrace import MultiChessTrace

class TrainChessEnvironment:
    __slots__ = ["__trace"]

    __trace: MultiChessTrace

    def __init__(self, trace: MultiChessTrace):
        self.__trace = trace

    async def move(self, action: Action) -> ActionResult:
        return self.__trace.move(action)

    async def reset(self, state: State) -> Dict[str, bool]:
        return {"success": self.__trace.reset(state)}
