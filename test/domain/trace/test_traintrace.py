# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest

from domain.dto.traindto import State
from domain.microchess import MicroBoard
from domain.trace.traintrace import ChessTrainTrace

from test.constant import MICRO_K_FEN

@pytest.mark.asyncio
async def test_reset() -> None:
    trace: ChessTrainTrace = ChessTrainTrace()
    state: State = State(fens=[MICRO_K_FEN])
    result: bool = trace.reset(state)
    reseted: ChessTrainTrace = ChessTrainTrace([MicroBoard(MICRO_K_FEN)])

    assert result == True
    assert trace == reseted
