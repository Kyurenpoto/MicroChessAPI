# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Optional

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from domain.dto.testdto import Action, State
from application.chessenv.testenv import ChessTestEnvironment

router: APIRouter = APIRouter(prefix="/tests")
env: ChessTestEnvironment = ChessTestEnvironment()

@router.put("/action", status_code=status.HTTP_200_OK)
async def action(action: Action) -> JSONResponse:
    try:
        return JSONResponse(content=jsonable_encoder(await env.move(action)))
    except RuntimeError as ex:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"msg": "\n".join(ex.args)})

@router.post("/state", status_code=status.HTTP_201_CREATED)
async def state(state: State) -> Optional[JSONResponse]:
    try:
        await env.reset(state)
    except RuntimeError as ex:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"msg": "\n".join(ex.args)})
