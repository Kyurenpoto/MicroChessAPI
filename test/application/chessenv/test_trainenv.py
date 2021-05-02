# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

import pytest

from domain.dto.traindto import Action, ActionResult, State
from domain.microchess import MICRO_STARTING_FEN
from domain.trace.traintrace import Fake
from application.chessenv.trainenv import TrainChessEnvironment

@pytest.mark.asyncio
async def test_move() -> None:
    env: TrainChessEnvironment = TrainChessEnvironment(Fake())
    result: ActionResult = await env.move(Action(
        fens=[MICRO_STARTING_FEN],
        moves=[]))
    assert result == ActionResult(
        fens=[MICRO_STARTING_FEN],
        statuses=[],
        next_move_lists=[])

@pytest.mark.asyncio
async def test_reset() -> None:
    env: TrainChessEnvironment = TrainChessEnvironment(Fake())
    state: State = State(fens=[MICRO_STARTING_FEN])
    result: Dict[str, bool] = await env.reset(state)
    assert result == {"success": True}
