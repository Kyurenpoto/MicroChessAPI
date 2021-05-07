# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from httpx import AsyncClient
from fastapi import status

from domain.implementation.microsan import MICRO_FIRST_MOVE_SAN
from domain.implementation.microboard import MICRO_STARTING_FEN, MICRO_FIRST_MOVE_FEN
from domain.implementation.legalsan import MICRO_FIRST_LEGAL_MOVES
from main import app

@pytest.mark.asyncio
async def test_model_act() -> None:
    client = AsyncClient(app=app, base_url="http://test")
    response = await client.put(
        url="/model/act",
        json={"fens": [MICRO_STARTING_FEN],
        "sans": [MICRO_FIRST_MOVE_SAN]})
    await client.aclose()

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "fens": [MICRO_FIRST_MOVE_FEN],
        "statuses": [0],
        "legal_moves": [MICRO_FIRST_LEGAL_MOVES]}
