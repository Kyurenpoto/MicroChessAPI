# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from domain.dto.modeldto import ModelRequest
from application.chessenv.modelenv import ChessEnvironment

router: APIRouter = APIRouter(prefix="/model")
env: ChessEnvironment = ChessEnvironment()

@router.put("/act", status_code=status.HTTP_200_OK)
async def act(request: ModelRequest) -> JSONResponse:
    try:
        return JSONResponse(content=jsonable_encoder(await env.act(request)))
    except RuntimeError as ex:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"msg": "\n".join(ex.args)})
