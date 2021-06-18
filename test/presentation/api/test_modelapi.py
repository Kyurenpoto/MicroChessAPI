# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from fastapi import status
from httpx import AsyncClient
from src.domain.error.dtoerror import EmptyFENs, EmptySANs, NotMatchedNumberFENsSANs
from src.domain.implementation.basictype import FEN, SAN
from src.domain.implementation.legalsan import LegalSANs
from submodules.fastapi_haljson.src.halmodel import HALBase


@pytest.mark.asyncio
async def test_fen_status_normal(async_client: AsyncClient) -> None:
    response = await async_client.post(
        url="/model/fen-status",
        json={"fens": [FEN.starting()]},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "links": {
            rel: {"href": url.href}
            for rel, url in HALBase.from_routes_with_requested(
                {
                    "fen-status": "/model/fen-status",
                    "next-fen": "/model/next-fen",
                },
                "fen-status",
                "post",
            ).links.items()
        },
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
        json={"fens": [FEN.starting()], "sans": [SAN.first_move()]},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "links": {
            rel: {"href": url.href}
            for rel, url in HALBase.from_routes_with_requested(
                {
                    "fen-status": "/model/fen-status",
                    "next-fen": "/model/next-fen",
                },
                "next-fen",
                "post",
            ).links.items()
        },
        "next_fens": [FEN.first_move()],
    }


@pytest.mark.asyncio
async def test_next_fen_empty_FENs(async_client: AsyncClient) -> None:
    response = await async_client.post(url="/model/next-fen", json={"fens": [], "sans": [SAN.first_move()]})

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
        ({"fens": [FEN.starting(), FEN.starting()], "sans": [SAN.first_move()]}),
        ({"fens": [FEN.starting()], "sans": [SAN.first_move(), SAN.first_move()]}),
    ],
)
async def test_next_fen_not_matched_number_FENs_SANs(async_client: AsyncClient, json: dict[str, list[str]]) -> None:
    response = await async_client.post(url="/model/next-fen", json=json)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    print(response.json())
    assert response.json()["error"] == NotMatchedNumberFENsSANs.error_type()
