# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.testdto import ActionResult, State, Action
from domain.microchess import MICRO_STARTING_FEN, MicroBoard, MicroBoardStatus
from domain.trace.testtrace import ChessTestTrace

from test.constant import MICRO_FIRST_MOVE_FEN, MICRO_FIRST_MOVE_SAN, MICRO_FIRST_NEXT_MOVE_LIST, MICRO_K_FEN

def test_move() -> None:
    trace: ChessTestTrace = ChessTestTrace()
    action: Action = Action(fen=MICRO_STARTING_FEN, san=MICRO_FIRST_MOVE_SAN)
    result: ActionResult = trace.move(action)
    
    assert result == ActionResult(
        fen=MICRO_FIRST_MOVE_FEN,
        status=MicroBoardStatus.NONE.value,
        next_move_list=MICRO_FIRST_NEXT_MOVE_LIST)

def test_reset() -> None:
    trace: ChessTestTrace = ChessTestTrace()
    state: State = State(fen=MICRO_K_FEN)
    trace.reset(state)
    
    reseted: ChessTestTrace = ChessTestTrace(MicroBoard(MICRO_K_FEN))

    assert trace == reseted
