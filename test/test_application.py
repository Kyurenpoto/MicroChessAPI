# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

import pytest

from application import tests as apptests, trains as apptrains
from domain.dto import tests as dtotests, trains as dtotrains

from domain.microchess import MicroBoardStatus, MICRO_STARTING_FEN

@pytest.mark.asyncio
async def test_tests_move() -> None:
    fake: apptests.Fake = apptests.Fake()
    result: dtotests.ActionResult = await fake.move(dtotests.Action(
        fen=MICRO_STARTING_FEN,
        move=""))
    assert result == dtotests.ActionResult(
        fen=MICRO_STARTING_FEN,
        status=MicroBoardStatus.NONE.value,
        next_move_list=[])

@pytest.mark.asyncio
async def test_trains_move() -> None:
    fake: apptrains.Fake = apptrains.Fake()
    result: dtotrains.ActionResult = await fake.move(dtotrains.Action(
        fens=[MICRO_STARTING_FEN],
        moves=[]))
    assert result == dtotrains.ActionResult(
        fens=[MICRO_STARTING_FEN],
        statuses=[],
        next_move_lists=[])

@pytest.mark.asyncio
async def test_tests_reset() -> None:
    fake: apptests.Fake = apptests.Fake()
    state: dtotests.State = dtotests.State(fen=MICRO_STARTING_FEN)
    result: Dict[str, bool] = await fake.reset(state)
    assert result == {"success": True}

@pytest.mark.asyncio
async def test_trains_reset() -> None:
    fake: apptrains.Fake = apptrains.Fake()
    state: dtotrains.State = dtotrains.State(fens=[MICRO_STARTING_FEN])
    result: Dict[str, bool] = await fake.reset(state)
    assert result == {"success": True}
