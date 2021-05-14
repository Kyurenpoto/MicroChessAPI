# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from application.chessenv.modelenv import ChessEnvironment
from domain.dto.modeldto import ModelNextFENRequest, ModelNextFENResponse
from domain.implementation.legalsan import MICRO_FIRST_LEGAL_MOVES
from domain.implementation.movedfen import MICRO_FIRST_MOVE_FEN, MICRO_STARTING_FEN
from domain.implementation.validmicrosan import MICRO_FIRST_MOVE_SAN
from domain.model import Fake


@pytest.mark.asyncio
async def test_next_fen() -> None:
    env: ChessEnvironment = ChessEnvironment(Fake())
    request: ModelNextFENRequest = ModelNextFENRequest(fens=[MICRO_STARTING_FEN], sans=[MICRO_FIRST_MOVE_SAN])
    response: ModelNextFENResponse = await env.next_fen(request)

    assert response == ModelNextFENResponse(
        fens=[MICRO_FIRST_MOVE_FEN], statuses=[0], legal_moves=[MICRO_FIRST_LEGAL_MOVES]
    )
