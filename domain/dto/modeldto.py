# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List

from pydantic import BaseModel

from domain.microchess import MicroBoardStatus

class ModelRequest(BaseModel):
    fens: List[str]
    sans: List[str]

class ModelResponse(BaseModel):
    fens: List[str]
    statuses: List[MicroBoardStatus]
    legal_moves: List[List[str]]