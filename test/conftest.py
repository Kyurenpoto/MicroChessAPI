# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from httpx import AsyncClient
from main import app, unwire, wire
from src.config import Container


@pytest.fixture
async def async_client() -> AsyncClient:
    wire()
    client = AsyncClient(app=app, base_url="http://test")
    yield client
    await client.aclose()


@pytest.fixture
async def container() -> Container:
    wire()
    yield app.state.container
    unwire()
