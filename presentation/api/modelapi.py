# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from application.chessenv.modelenv import ChessEnvironment
from domain.dto.modeldto import ModelNextFENRequest
from domain.implementation.validmodeldto import ValidModelNextFENRequest
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router: APIRouter = APIRouter(prefix="/model")
env: ChessEnvironment = ChessEnvironment()


@router.post("/fen-status", status_code=status.HTTP_200_OK)
async def fen_status(request: ModelNextFENRequest) -> JSONResponse:
    return None


@router.post("/next-fen", status_code=status.HTTP_200_OK)
async def next_fen(request: ModelNextFENRequest) -> JSONResponse:
    try:
        return JSONResponse(content=jsonable_encoder(await env.next_fen(ValidModelNextFENRequest(request).value())))
    except RuntimeError as ex:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder(ex.args[0]))
