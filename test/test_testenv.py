# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

import pytest

from domain.dto import tests as dtotests
from application import testenv

from domain.microchess import MicroBoardStatus, MICRO_STARTING_FEN

@pytest.mark.asyncio
async def test_move() -> None:
    fake: testenv.Fake = testenv.Fake()
    result: dtotests.ActionResult = await fake.move(dtotests.Action(
        fen=MICRO_STARTING_FEN,
        move=""))
    assert result == dtotests.ActionResult(
        fen=MICRO_STARTING_FEN,
        status=MicroBoardStatus.NONE.value,
        next_move_list=[])

@pytest.mark.asyncio
async def test_reset() -> None:
    fake: testenv.Fake = testenv.Fake()
    state: dtotests.State = dtotests.State(fen=MICRO_STARTING_FEN)
    result: Dict[str, bool] = await fake.reset(state)
    assert result == {"success": True}
