# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, List

import pytest
from domain.implementation.legalsan import MICRO_FIRST_LEGAL_MOVES
from domain.implementation.microboard import MICRO_FIRST_MOVE_FEN, MICRO_STARTING_FEN
from domain.implementation.microsan import MICRO_FIRST_MOVE_SAN
from fastapi import status
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_model_act_200(async_client: AsyncClient) -> None:
    response = await async_client.put(
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
@pytest.mark.parametrize(
    "json",
    [
        (
            {
                "fens": [MICRO_STARTING_FEN, MICRO_STARTING_FEN],
                "sans": [MICRO_FIRST_MOVE_SAN],
            }
        ),
        (
            {
                "fens": [MICRO_STARTING_FEN],
                "sans": [MICRO_FIRST_MOVE_SAN, MICRO_FIRST_MOVE_SAN],
            }
        ),
        ({"fens": [MICRO_STARTING_FEN], "sans": []}),
        ({"fens": [], "sans": [MICRO_FIRST_MOVE_SAN]}),
    ],
)
async def test_model_act_400(async_client: AsyncClient, json: Dict[str, List], msg: str) -> None:
    response = await async_client.put(url="/model/act", json=json)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
