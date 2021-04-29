# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List

from .microchess import MicroBoard, MicroBoardStatus
from .dto import tests, trains

class TestsTrace:
    __slots__ = ["__board"]
    
    __board: MicroBoard

    def __init__(self):
        self.__board = None

    def move(self, action: tests.Action) -> tests.ActionResult:
        return tests.ActionResult(fen="", status=MicroBoardStatus.NONE, next_move_list=[])

    def reset(self, state: tests.State) -> bool:
        return True

class TrainsTrace:
    __slots__ = ["__boards"]
    
    __boards: List[MicroBoard]

    def __init__(self):
        self.__boards = None

    def move(self, action: trains.Action) -> trains.ActionResult:
        return trains.ActionResult(fens=[], statuses=[], next_move_lists=[])

    def reset(self, state: trains.State) -> bool:
        return True
