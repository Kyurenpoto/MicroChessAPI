# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List, Dict

from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from domain import microchess

app: FastAPI = FastAPI()

class ActionTest(BaseModel):
    fen: str
    move: str
class ActionTestResult(BaseModel):
    fen: str
    status: microchess.MicroBoardStatus
    next_move_list: List[str]

async def move_on_test(action: ActionTest) -> Dict:
    result: ActionTestResult = ActionTestResult(fen="", status=microchess.MicroBoardStatus.NONE, next_move_list=[])
    return jsonable_encoder(result)

@app.put("/action-test", status_code=status.HTTP_200_OK)
async def action_test(action: ActionTest) -> JSONResponse:
    return JSONResponse(content=await move_on_test(action))

class ActionTrain(BaseModel):
    fens: str
    moves: str

class ActionTrainResult(BaseModel):
    fens: List[str]
    statuses: List[microchess.MicroBoardStatus]
    next_move_lists: List[List[str]]

async def move_on_train(action: ActionTrain) -> Dict:
    result: ActionTrainResult = ActionTrainResult(fens=[], statuses=[], next_move_lists=[])
    return jsonable_encoder(result)

@app.put("/action-train", status_code=status.HTTP_200_OK)
async def action_train(action: ActionTrain) -> JSONResponse:
    return JSONResponse(content=await move_on_train(action))

class StateTest(BaseModel):
    fen: str

async def reset_on_test(state: StateTest) -> Dict[str, bool]:
    return { "success": True }

@app.post("/state-test", status_code=status.HTTP_201_CREATED)
async def state_test(state: StateTest) -> Dict[str, bool]:
    return await reset_on_test(state)

class StateTrain(BaseModel):
    fens: str

async def reset_on_train(state: StateTrain) -> Dict[str, bool]:
    return { "success": True }

@app.post("/state-train", status_code=status.HTTP_201_CREATED)
async def state_train(state: StateTrain) -> Dict[str, bool]:
    return await reset_on_train(state)
