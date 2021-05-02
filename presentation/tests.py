# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Union, Dict

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

@router.post("/state", status_code=status.HTTP_201_CREATED)
async def state(state: State) -> Union[Dict[str, bool], JSONResponse]:
    result: Dict[str, bool] = await tests.reset(state)
    if result["success"] is True:
        return result
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"msg": "Invalid FEN"})