# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from httpx import AsyncClient
from fastapi import status

from main import app

client = AsyncClient(app=app, base_url="http://test")

@pytest.mark.asyncio
async def test_tests_action():
    response = await client.put(url="/tests/action", json={"fen": "", "move": ""})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"fen": "", "status": 0, "next_move_list": []}

@pytest.mark.asyncio
async def test_trains_action():
    response = await client.put(url="/trains/action", json={"fens": [], "moves": []})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"fens": [], "statuses": [], "next_move_lists": []}

@pytest.mark.asyncio
async def test_tests_state():
    response = await client.post(url="/tests/state", json={"fen": ""})
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.asyncio
async def test_trains_state():
    response = await client.post(url="/trains/state", json={"fens": []})
    assert response.status_code == status.HTTP_201_CREATED
