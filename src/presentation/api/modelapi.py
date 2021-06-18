# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from fastapi import APIRouter, status
from src.application.createdresponse import CreatedFENStatusResponse, CreatedNextFENResponse
from src.domain.dto.modeldto import ModelFENStatusRequest, ModelNextFENRequest
from src.presentation.response import ExceptionHandledResponse, HALJSONResponse

router: APIRouter = APIRouter(prefix="/model")


@router.post(
    "/fen-status",
    name="fen-status",
    description="The status and legal moves of the requested FEN",
    status_code=status.HTTP_200_OK,
)
async def fen_status(request: ModelFENStatusRequest) -> HALJSONResponse:
    return ExceptionHandledResponse(CreatedFENStatusResponse(request)).handled()


@router.post(
    "/next-fen",
    name="next-fen",
    description="FEN as a result of applying requested SAN to requested FEN",
    status_code=status.HTTP_200_OK,
)
async def next_fen(request: ModelNextFENRequest) -> HALJSONResponse:
    return ExceptionHandledResponse(CreatedNextFENResponse(request)).handled()
