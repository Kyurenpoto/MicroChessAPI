# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List, Dict

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from domain import microchess

router: APIRouter = APIRouter(prefix="/tests")

class ActionTest(BaseModel):
    fen: str
    move: str

class ActionTestResult(BaseModel):
    fen: str
    status: microchess.MicroBoardStatus
    next_move_list: List[str]

async def move(action: ActionTest) -> Dict:
    result: ActionTestResult = ActionTestResult(fen="", status=microchess.MicroBoardStatus.NONE, next_move_list=[])
    return jsonable_encoder(result)

@router.put("/action", status_code=status.HTTP_200_OK)
async def action(action: ActionTest) -> JSONResponse:
    return JSONResponse(content=await move(action))

class StateTest(BaseModel):
    fen: str

async def reset(state: StateTest) -> Dict[str, bool]:
    return { "success": True }

@router.post("/state", status_code=status.HTTP_201_CREATED)
async def state(state: StateTest) -> Dict[str, bool]:
    return await reset(state)

