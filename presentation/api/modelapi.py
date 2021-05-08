# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from application.chessenv.modelenv import ChessEnvironment
from domain.dto.modeldto import ModelRequest
from domain.dto.validmodeldto import ValidModelRequest
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router: APIRouter = APIRouter(prefix="/model")
env: ChessEnvironment = ChessEnvironment()


@router.post("/act", status_code=status.HTTP_200_OK)
async def act(request: ModelRequest) -> JSONResponse:
    try:
        return JSONResponse(content=jsonable_encoder(await env.act(ValidModelRequest(request).value())))
    except RuntimeError as ex:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": ex.args[0]})
