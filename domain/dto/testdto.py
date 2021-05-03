# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List

from pydantic import BaseModel

from domain.microchess import MicroBoardStatus

class Action(BaseModel):
    fen: str
    san: str

class ActionResult(BaseModel):
    fen: str
    status: MicroBoardStatus
    next_move_list: List[str]

class State(BaseModel):
    fen: str
