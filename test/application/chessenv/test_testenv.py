# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

import pytest

from domain.dto.testdto import Action, ActionResult, State
from domain.microchess import MicroBoardStatus, MICRO_STARTING_FEN
from domain.trace.testtrace import Fake
from application.chessenv.testenv import ChessTestEnvironment

from test.constant import MICRO_FIRST_MOVE_FEN, MICRO_FIRST_MOVE_SAN, MICRO_FIRST_NEXT_MOVE_LIST

@pytest.mark.asyncio
async def test_move() -> None:
    env: ChessTestEnvironment = ChessTestEnvironment(Fake())
    result: ActionResult = await env.move(Action(
        fen=MICRO_STARTING_FEN,
        san=MICRO_FIRST_MOVE_SAN))
        
    assert result == ActionResult(
        fen=MICRO_FIRST_MOVE_FEN,
        status=MicroBoardStatus.NONE.value,
        next_move_list=MICRO_FIRST_NEXT_MOVE_LIST)

@pytest.mark.asyncio
async def test_reset() -> None:
    env: ChessTestEnvironment = ChessTestEnvironment(Fake())
    state: State = State(fen=MICRO_STARTING_FEN)
    result: Dict[str, bool] = await env.reset(state)

    assert result == {"success": True}
