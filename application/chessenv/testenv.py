# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

from domain.dto.testdto import Action, ActionResult, State
from domain.trace.testtrace import SingleChessTrace

class ChessTestEnvironment:
    __slots__ = ["__trace"]

    __trace: SingleChessTrace

    def __init__(self, trace: SingleChessTrace):
        self.__trace = trace

    async def move(self, action: Action) -> ActionResult:
        return self.__trace.move(action)

    async def reset(self, state: State) -> Dict[str, bool]:
        return {"success": self.__trace.reset(state)}
