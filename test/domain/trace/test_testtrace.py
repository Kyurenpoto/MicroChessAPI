# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.testdto import State
from domain.microchess import MicroBoard
from domain.trace.testtrace import ChessTestTrace

from test.constant import MICRO_K_FEN

def test_reset() -> None:
    trace: ChessTestTrace = ChessTestTrace()
    state: State = State(fen=MICRO_K_FEN)
    trace.reset(state)
    
    reseted: ChessTestTrace = ChessTestTrace(MicroBoard(MICRO_K_FEN))

    assert trace == reseted
