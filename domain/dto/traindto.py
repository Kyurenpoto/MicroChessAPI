# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List

from pydantic import BaseModel

from domain.microchess import MicroBoardStatus

class Action(BaseModel):
    fens: List[str]
    sans: List[str]

class ActionResult(BaseModel):
    fens: List[str]
    statuses: List[MicroBoardStatus]
    next_move_lists: List[List[str]]

class State(BaseModel):
    fens: List[str]
