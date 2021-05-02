# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

import pytest

from domain.dto.traindto import Action, ActionResult, State
from application.chessenv.trainenv import Fake

from domain.microchess import MICRO_STARTING_FEN

@pytest.mark.asyncio
async def test_move() -> None:
    fake: Fake = Fake()
    result: ActionResult = await fake.move(Action(
        fens=[MICRO_STARTING_FEN],
        moves=[]))
    assert result == ActionResult(
        fens=[MICRO_STARTING_FEN],
        statuses=[],
        next_move_lists=[])

@pytest.mark.asyncio
async def test_reset() -> None:
    fake: Fake = Fake()
    state: State = State(fens=[MICRO_STARTING_FEN])
    result: Dict[str, bool] = await fake.reset(state)
    assert result == {"success": True}
