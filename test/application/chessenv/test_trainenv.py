# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest

from domain.dto.traindto import Action, ActionResult, State
from domain.microchess import MicroBoardStatus, MICRO_STARTING_FEN
from domain.trace.traintrace import Fake
from application.chessenv.trainenv import ChessTrainEnvironment

from test.constant import MICRO_FIRST_MOVE_FEN, MICRO_FIRST_MOVE_SAN, MICRO_FIRST_NEXT_MOVE_LIST

@pytest.mark.asyncio
async def test_move() -> None:
    env: ChessTrainEnvironment = ChessTrainEnvironment(Fake())
    result: ActionResult = await env.move(Action(
        fens=[MICRO_STARTING_FEN],
        sans=[MICRO_FIRST_MOVE_SAN]))

    assert result == ActionResult(
        fens=[MICRO_FIRST_MOVE_FEN],
        statuses=[MicroBoardStatus.NONE],
        next_move_lists=[MICRO_FIRST_NEXT_MOVE_LIST])

@pytest.mark.asyncio
async def test_reset() -> None:
    env: ChessTrainEnvironment = ChessTrainEnvironment(Fake())
    state: State = State(fens=[MICRO_STARTING_FEN])
    await env.reset(state)
