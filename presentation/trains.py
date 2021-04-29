# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List, Dict

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from domain import microchess

router: APIRouter = APIRouter(prefix="/trains")

class ActionTrain(BaseModel):
    fens: str
    moves: str

class ActionTrainResult(BaseModel):
    fens: List[str]
    statuses: List[microchess.MicroBoardStatus]
    next_move_lists: List[List[str]]

async def move(action: ActionTrain) -> Dict:
    result: ActionTrainResult = ActionTrainResult(fens=[], statuses=[], next_move_lists=[])
    return jsonable_encoder(result)

@router.put("/action", status_code=status.HTTP_200_OK)
async def action(action: ActionTrain) -> JSONResponse:
    return JSONResponse(content=await move(action))

class StateTrain(BaseModel):
    fens: str

async def reset(state: StateTrain) -> Dict[str, bool]:
    return { "success": True }

@router.post("/state", status_code=status.HTTP_201_CREATED)
async def state(state: StateTrain) -> Dict[str, bool]:
    return await reset(state)

