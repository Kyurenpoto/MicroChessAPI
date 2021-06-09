# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from application.createdresponse import CreatedFENStatusResponse, CreatedNextFENResponse
from domain.dto.modeldto import ModelFENStatusRequest, ModelNextFENRequest
from fastapi import APIRouter, status
from presentation.response import ExceptionHandledResponse, HALJSONResponse

router: APIRouter = APIRouter(prefix="/model")


@router.post(
    "/fen-status", status_code=status.HTTP_200_OK, description="The status and legal moves of the requested FEN"
)
async def fen_status(request: ModelFENStatusRequest) -> HALJSONResponse:
    return ExceptionHandledResponse(CreatedFENStatusResponse(request)).handled()


@router.post(
    "/next-fen",
    status_code=status.HTTP_200_OK,
    description="FEN as a result of applying requested SAN to requested FEN",
)
async def next_fen(request: ModelNextFENRequest) -> HALJSONResponse:
    return ExceptionHandledResponse(CreatedNextFENResponse(request)).handled()
