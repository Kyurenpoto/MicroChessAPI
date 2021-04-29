# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

import pytest

from application import tests as apptests, trains as apptrains
from domain.dto import tests as dtotests, trains as dtotrains

from domain.microchess import MicroBoardStatus

@pytest.mark.asyncio
async def test_tests_move():
    fake: apptests.Fake = apptests.Fake()
    result: dtotests.ActionResult = await fake.move(dtotests.Action(fen="", move=""))
    assert result == dtotests.ActionResult(fen="", status=MicroBoardStatus.NONE.value, next_move_list=[])

@pytest.mark.asyncio
async def test_trains_move():
    fake: apptrains.Fake = apptrains.Fake()
    result: dtotrains.ActionResult = await fake.move(dtotrains.Action(fens=[], moves=[]))
    assert result == dtotrains.ActionResult(fens=[], statuses=[], next_move_lists=[])

@pytest.mark.asyncio
async def test_tests_reset():
    fake: apptests.Fake = apptests.Fake()
    result: Dict[str, bool] = await fake.reset(dtotests.State(fen=""))
    assert result == {"success": True}

@pytest.mark.asyncio
async def test_trains_reset():
    fake: apptrains.Fake = apptrains.Fake()
    result: Dict[str, bool] = await fake.reset(dtotrains.State(fens=[]))
    assert result == {"success": True}
