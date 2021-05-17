# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from application.chessenv.modelenv import MicroChessEnvironment
from domain.dto.modeldto import ModelFENStatusRequest, ModelFENStatusResponse, ModelNextFENRequest, ModelNextFENResponse
from domain.implementation.legalsan import MICRO_INITIAL_LEGAL_MOVES
from domain.implementation.validmicrofen import MICRO_FIRST_MOVE_FEN, MICRO_STARTING_FEN
from domain.implementation.validmicrosan import MICRO_FIRST_MOVE_SAN
from domain.model import Fake


@pytest.mark.asyncio
async def test_fen_status() -> None:
    env: MicroChessEnvironment = MicroChessEnvironment(Fake())
    request: ModelFENStatusRequest = ModelFENStatusRequest(fens=[MICRO_STARTING_FEN])
    response: ModelFENStatusResponse = await env.fen_status(request)

    assert response == ModelFENStatusResponse(statuses=[1], legal_moves=[MICRO_INITIAL_LEGAL_MOVES])


@pytest.mark.asyncio
async def test_next_fen() -> None:
    env: MicroChessEnvironment = MicroChessEnvironment(Fake())
    request: ModelNextFENRequest = ModelNextFENRequest(fens=[MICRO_STARTING_FEN], sans=[MICRO_FIRST_MOVE_SAN])
    response: ModelNextFENResponse = await env.next_fen(request)

    assert response == ModelNextFENResponse(next_fens=[MICRO_FIRST_MOVE_FEN])
