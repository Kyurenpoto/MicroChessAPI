# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from httpx import AsyncClient
from fastapi import status

from domain.microchess import MICRO_STARTING_FEN
from main import app

@pytest.mark.asyncio
async def test_tests_action() -> None:
    client = AsyncClient(app=app, base_url="http://test")
    response = await client.put(
        url="/tests/action",
        json={"fen": MICRO_STARTING_FEN,
        "move": ""})
    await client.aclose()

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "fen": MICRO_STARTING_FEN,
        "status": 0,
        "next_move_list": []}

@pytest.mark.asyncio
async def test_tests_state() -> None:
    client = AsyncClient(app=app, base_url="http://test")
    response = await client.post(
        url="/tests/state",
        json={"fen": MICRO_STARTING_FEN})
    await client.aclose()
        
    assert response.status_code == status.HTTP_201_CREATED
