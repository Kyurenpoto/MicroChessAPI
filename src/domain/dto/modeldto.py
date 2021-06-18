# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Union

from pydantic import BaseModel
from submodules.fastapi_haljson.src.halmodel import HALBase


class ModelInternal(BaseModel):
    routes: dict[str, str]


class ModelAPIInfo(BaseModel):
    name: str
    method: str


class ModelNextFENRequest(BaseModel):
    fens: list[str]
    sans: list[str]


class ModelNextFENResponse(HALBase):
    next_fens: list[str]


class ModelFENStatusRequest(BaseModel):
    fens: list[str]


class ModelFENStatusResponse(HALBase):
    statuses: list[int]
    legal_moves: list[list[str]]


class ModelErrorResponse(BaseModel):
    message: str
    location: str
    param: str
    value: Union[list[str], list[list[str]]]
    error: str
