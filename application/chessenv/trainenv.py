# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.traindto import Action, ActionResult, State
from domain.trace.traintrace import ChessMultiTrace, ChessTrainTrace

class ChessTrainEnvironment:
    __slots__ = ["__trace"]

    __trace: ChessMultiTrace

    def __init__(self, trace: ChessMultiTrace = ChessTrainTrace()):
        self.__trace = trace

    async def move(self, action: Action) -> ActionResult:
        return self.__trace.move(action)

    async def reset(self, state: State) -> None:
        self.__trace.reset(state)
