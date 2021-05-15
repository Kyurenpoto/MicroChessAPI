# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from application.chessenv.modelenv import ChessEnvironment
from domain.dto.modeldto import ModelFENStatusRequest, ModelNextFENRequest
from domain.implementation.validmodeldto import ValidModelFENStatusRequest, ValidModelNextFENRequest
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router: APIRouter = APIRouter(prefix="/model")
env: ChessEnvironment = ChessEnvironment()


@router.post(
    "/fen-status", status_code=status.HTTP_200_OK, description="The status and legal moves of the requested FEN"
)
async def fen_status(request: ModelFENStatusRequest) -> JSONResponse:
    try:
        return JSONResponse(content=jsonable_encoder(await env.fen_status(ValidModelFENStatusRequest(request).value())))
    except RuntimeError as ex:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder(ex.args[0]))


@router.post(
    "/next-fen",
    status_code=status.HTTP_200_OK,
    description="FEN as a result of applying requested SAN to requested FEN",
)
async def next_fen(request: ModelNextFENRequest) -> JSONResponse:
    try:
        return JSONResponse(content=jsonable_encoder(await env.next_fen(ValidModelNextFENRequest(request).value())))
    except RuntimeError as ex:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder(ex.args[0]))
