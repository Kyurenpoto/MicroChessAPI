# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List, Union

from pydantic import BaseModel


class ModelNextFENRequest(BaseModel):
    fens: List[str]
    sans: List[str]


class ModelNextFENResponse(BaseModel):
    fens: List[str]
    statuses: List[int]
    legal_moves: List[List[str]]


class ModelErrorResponse(BaseModel):
    message: str
    location: str
    param: str
    value: Union[List[str], List[List[str]]]
    error: str
