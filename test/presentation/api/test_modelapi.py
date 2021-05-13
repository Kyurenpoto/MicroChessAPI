# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, List

import pytest
from domain.error.dtoerror import ERROR_TYPE_EMPTY_FENS, ERROR_TYPE_EMPTY_SANS, ERROR_TYPE_NOT_MATCHED_NUMBER_FENS_SANS
from domain.implementation.legalsan import MICRO_FIRST_LEGAL_MOVES
from domain.implementation.movedfen import MICRO_FIRST_MOVE_FEN, MICRO_STARTING_FEN
from domain.implementation.validmicrosan import MICRO_FIRST_MOVE_SAN
from fastapi import status
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_normal(async_client: AsyncClient) -> None:
    response = await async_client.post(
        url="/model/act",
        json={"fens": [MICRO_STARTING_FEN], "sans": [MICRO_FIRST_MOVE_SAN]},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "fens": [MICRO_FIRST_MOVE_FEN],
        "statuses": [0],
        "legal_moves": [MICRO_FIRST_LEGAL_MOVES],
    }


@pytest.mark.asyncio
async def test_empty_FENs(async_client: AsyncClient) -> None:
    response = await async_client.post(url="/model/act", json={"fens": [], "sans": [MICRO_FIRST_MOVE_SAN]})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["error"] == ERROR_TYPE_EMPTY_FENS


@pytest.mark.asyncio
async def test_empty_SANs(async_client: AsyncClient) -> None:
    response = await async_client.post(url="/model/act", json={"fens": [MICRO_STARTING_FEN], "sans": []})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["error"] == ERROR_TYPE_EMPTY_SANS


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "json",
    [
        ({"fens": [MICRO_STARTING_FEN, MICRO_STARTING_FEN], "sans": [MICRO_FIRST_MOVE_SAN]}),
        ({"fens": [MICRO_STARTING_FEN], "sans": [MICRO_FIRST_MOVE_SAN, MICRO_FIRST_MOVE_SAN]}),
    ],
)
async def test_not_matched_number_FENs_SANs(async_client: AsyncClient, json: Dict[str, List[str]]) -> None:
    response = await async_client.post(url="/model/act", json=json)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    print(response.json())
    assert response.json()["error"] == ERROR_TYPE_NOT_MATCHED_NUMBER_FENS_SANS
