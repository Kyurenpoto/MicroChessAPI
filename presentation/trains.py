# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from domain.dto.tests import Action, ActionResult, State

router: APIRouter = APIRouter(prefix="/trains")

async def move(action: Action) -> Dict:
    result: ActionResult = ActionResult(fens=[], statuses=[], next_move_lists=[])
    return jsonable_encoder(result)

@router.put("/action", status_code=status.HTTP_200_OK)
async def action(action: Action) -> JSONResponse:
    return JSONResponse(content=await move(action))

async def reset(state: State) -> Dict[str, bool]:
    return { "success": True }

@router.post("/state", status_code=status.HTTP_201_CREATED)
async def state(state: State) -> Dict[str, bool]:
    return await reset(state)

