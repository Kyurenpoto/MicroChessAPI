# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, List

import pytest
from domain.error.emptyfens import MSG_EMPTY_FENS
from domain.error.emptysans import MSG_EMPTY_SANS
from domain.error.notmatchednumberfenssans import MSG_NOT_MATCHED_NUMBER_FENS_SANS
from domain.implementation.legalsan import MICRO_FIRST_LEGAL_MOVES
from domain.implementation.microboard import MICRO_FIRST_MOVE_FEN, MICRO_STARTING_FEN
from domain.implementation.microsan import MICRO_FIRST_MOVE_SAN
from fastapi import status
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_model_act_200(async_client: AsyncClient) -> None:
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
@pytest.mark.parametrize(
    "json, message",
    [
        (
            {
                "fens": [MICRO_STARTING_FEN, MICRO_STARTING_FEN],
                "sans": [MICRO_FIRST_MOVE_SAN],
            },
            MSG_NOT_MATCHED_NUMBER_FENS_SANS,
        ),
        (
            {
                "fens": [MICRO_STARTING_FEN],
                "sans": [MICRO_FIRST_MOVE_SAN, MICRO_FIRST_MOVE_SAN],
            },
            MSG_NOT_MATCHED_NUMBER_FENS_SANS,
        ),
        ({"fens": [MICRO_STARTING_FEN], "sans": []}, MSG_EMPTY_SANS),
        ({"fens": [], "sans": [MICRO_FIRST_MOVE_SAN]}, MSG_EMPTY_FENS),
    ],
)
async def test_model_act_422(async_client: AsyncClient, json: Dict[str, List[str]], message: str) -> None:
    response = await async_client.post(url="/model/act", json=json)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"]["message"] == message
