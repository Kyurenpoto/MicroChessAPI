# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.traindto import Action, ActionResult, State
from domain.microchess import MICRO_STARTING_FEN, MicroBoard, MicroBoardStatus
from domain.trace.traintrace import ChessTrainTrace

from test.constant import MICRO_FIRST_MOVE_FEN, MICRO_FIRST_MOVE_SAN, MICRO_FIRST_NEXT_MOVE_LIST, MICRO_K_FEN

def test_move() -> None:
    trace: ChessTrainTrace = ChessTrainTrace()
    action: Action = Action(fens=[MICRO_STARTING_FEN], sans=[MICRO_FIRST_MOVE_SAN])
    result: ActionResult = trace.move(action)
    
    assert result == ActionResult(
        fens=[MICRO_FIRST_MOVE_FEN],
        statuses=[MicroBoardStatus.NONE],
        next_move_lists=[MICRO_FIRST_NEXT_MOVE_LIST])

def test_reset() -> None:
    trace: ChessTrainTrace = ChessTrainTrace()
    state: State = State(fens=[MICRO_K_FEN])
    trace.reset(state)
    
    reseted: ChessTrainTrace = ChessTrainTrace([MicroBoard(MICRO_K_FEN)])

    assert trace == reseted
