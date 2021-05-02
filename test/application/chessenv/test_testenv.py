# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

import pytest

from domain.dto.testdto import Action, ActionResult, State
from application.chessenv.testenv import Fake

from domain.microchess import MicroBoardStatus, MICRO_STARTING_FEN

@pytest.mark.asyncio
async def test_move() -> None:
    fake: Fake = Fake()
    result: ActionResult = await fake.move(Action(
        fen=MICRO_STARTING_FEN,
        move=""))
    assert result == ActionResult(
        fen=MICRO_STARTING_FEN,
        status=MicroBoardStatus.NONE.value,
        next_move_list=[])

@pytest.mark.asyncio
async def test_reset() -> None:
    fake: Fake = Fake()
    state: State = State(fen=MICRO_STARTING_FEN)
    result: Dict[str, bool] = await fake.reset(state)
    assert result == {"success": True}
