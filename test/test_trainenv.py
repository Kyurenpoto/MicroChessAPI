# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

import pytest

from domain.dto import trains as dtotrains
from application import trainenv

from domain.microchess import MICRO_STARTING_FEN

@pytest.mark.asyncio
async def test_move() -> None:
    fake: trainenv.Fake = trainenv.Fake()
    result: dtotrains.ActionResult = await fake.move(dtotrains.Action(
        fens=[MICRO_STARTING_FEN],
        moves=[]))
    assert result == dtotrains.ActionResult(
        fens=[MICRO_STARTING_FEN],
        statuses=[],
        next_move_lists=[])

@pytest.mark.asyncio
async def test_reset() -> None:
    fake: trainenv.Fake = trainenv.Fake()
    state: dtotrains.State = dtotrains.State(fens=[MICRO_STARTING_FEN])
    result: Dict[str, bool] = await fake.reset(state)
    assert result == {"success": True}
