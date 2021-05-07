# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest

from domain.dto.modeldto import ModelRequest, ModelResponse
from domain.microchess import MICRO_STARTING_FEN
from domain.model import Fake
from application.chessenv.modelenv import ChessEnvironment

from test.constant import MICRO_FIRST_MOVE_FEN, MICRO_FIRST_MOVE_SAN, MICRO_FIRST_LEGAL_MOVES

@pytest.mark.asyncio
async def test_act() -> None:
    env: ChessEnvironment = ChessEnvironment(Fake())
    request: ModelRequest = ModelRequest(fens=[MICRO_STARTING_FEN], sans=[MICRO_FIRST_MOVE_SAN])
    response: ModelResponse = await env.act(request)

    assert response == ModelResponse(
        fens=[MICRO_FIRST_MOVE_FEN],
        statuses=[0],
        legal_moves=[MICRO_FIRST_LEGAL_MOVES])
