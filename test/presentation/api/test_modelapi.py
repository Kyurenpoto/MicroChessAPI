# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from domain.error.dtoerror import EmptyFENs, EmptySANs, NotMatchedNumberFENsSANs
from domain.implementation.basictype import FEN
from domain.implementation.legalsan import LegalSANs
from domain.implementation.validmicrosan import MICRO_FIRST_MOVE_SAN
from fastapi import status
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_fen_status_normal(async_client: AsyncClient) -> None:
    response = await async_client.post(
        url="/model/fen-status",
        json={"fens": [FEN.starting()]},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "statuses": [1],
        "legal_moves": [LegalSANs.initial()],
    }


@pytest.mark.asyncio
async def test_fen_status_empty_FENs(async_client: AsyncClient) -> None:
    response = await async_client.post(url="/model/fen-status", json={"fens": []})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["error"] == EmptyFENs.error_type()


@pytest.mark.asyncio
async def test_next_fen_normal(async_client: AsyncClient) -> None:
    response = await async_client.post(
        url="/model/next-fen",
        json={"fens": [FEN.starting()], "sans": [MICRO_FIRST_MOVE_SAN]},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"next_fens": [FEN.first_move()]}


@pytest.mark.asyncio
async def test_next_fen_empty_FENs(async_client: AsyncClient) -> None:
    response = await async_client.post(url="/model/next-fen", json={"fens": [], "sans": [MICRO_FIRST_MOVE_SAN]})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["error"] == EmptyFENs.error_type()


@pytest.mark.asyncio
async def test_next_fen_empty_SANs(async_client: AsyncClient) -> None:
    response = await async_client.post(url="/model/next-fen", json={"fens": [FEN.starting()], "sans": []})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["error"] == EmptySANs.error_type()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "json",
    [
        ({"fens": [FEN.starting(), FEN.starting()], "sans": [MICRO_FIRST_MOVE_SAN]}),
        ({"fens": [FEN.starting()], "sans": [MICRO_FIRST_MOVE_SAN, MICRO_FIRST_MOVE_SAN]}),
    ],
)
async def test_next_fen_not_matched_number_FENs_SANs(async_client: AsyncClient, json: dict[str, list[str]]) -> None:
    response = await async_client.post(url="/model/next-fen", json=json)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    print(response.json())
    assert response.json()["error"] == NotMatchedNumberFENsSANs.error_type()
