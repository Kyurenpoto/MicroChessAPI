# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from domain.dto.tests import Action, State
from application.tests import Tests

router: APIRouter = APIRouter(prefix="/tests")
tests: Tests = Tests()

@router.put("/action", status_code=status.HTTP_200_OK)
async def action(action: Action) -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(await tests.move(action)))

class State(BaseModel):
    fen: str

@router.post("/state", status_code=status.HTTP_201_CREATED)
async def state(state: State) -> Dict[str, bool]:
    return await tests.reset(state)
