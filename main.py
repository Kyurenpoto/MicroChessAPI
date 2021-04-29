# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import List, Dict
from enum import Enum
import chess
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class MicroFen:
    __slots__ = ["__fen"]

    def __init__(self, fen: str):
        self.__fen = fen

    def __str__(self):
        return self.__fen

class MicroMove:
    def __init__(self, move: str):
        pass

class MicroBoardStatus(Enum):
    NONE = 0
    CHECKMATE = 1
    STALEMATE = 2

class MicroBoardBase(metaclass=ABCMeta):
    @abstractmethod
    def fen(self) -> MicroFen:
        pass

    @abstractmethod
    def move(self, move: MicroMove):
        pass

class MicroBoard(MicroBoardBase):
    def __init__(self, fen: MicroFen):
        pass

    def __init__(self, fen: str):
        self.__init__(MicroFen(fen))

    def fen(self) -> MicroFen:
        pass

    def move(self, move: MicroMove) -> MicroBoardBase:
        pass

boards: List[MicroBoard]

app: FastAPI = FastAPI()

class ActionTest(BaseModel):
    fen: str
    move: str

class ActionTestResult(BaseModel):
    fen: str
    status: MicroBoardStatus
    next_move_list: List[str]

@app.put("/action-test", status_code=status.HTTP_200_OK)
async def move_on_test(action: ActionTest) -> JSONResponse:
    result: ActionTestResult = ActionTestResult(fen="", status=MicroBoardStatus.NONE, next_move_list=[])
    return JSONResponse(content=jsonable_encoder(result))

class ActionTrain(BaseModel):
    fens: str
    moves: str

class ActionTrainResult(BaseModel):
    fens: List[str]
    statuses: List[MicroBoardStatus]
    next_move_lists: List[List[str]]

@app.put("/action-train", status_code=status.HTTP_200_OK)
async def move_on_train(action: ActionTrain) -> JSONResponse:
    result: ActionTrainResult = ActionTrainResult(fens=[], statuses=[], next_move_lists=[])
    return JSONResponse(content=jsonable_encoder(result))

class StateTest(BaseModel):
    fen: str

@app.post("/state-test", status_code=status.HTTP_201_CREATED)
async def reset_on_test(state: StateTest) -> Dict[str, bool]:
    return { "success": True }

class StateTrain(BaseModel):
    fens: str

@app.post("/state-train", status_code=status.HTTP_201_CREATED)
async def reset_on_train(state: StateTrain) -> Dict[str, bool]:
    return { "success": True }
