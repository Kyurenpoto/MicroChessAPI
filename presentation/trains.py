# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from domain.dto.trains import Action, State
from application.trains import move, reset

router: APIRouter = APIRouter(prefix="/trains")

@router.put("/action", status_code=status.HTTP_200_OK)
async def action(action: Action) -> JSONResponse:
    return JSONResponse(content=await move(action))

@router.post("/state", status_code=status.HTTP_201_CREATED)
async def state(state: State) -> Dict[str, bool]:
    return await reset(state)
