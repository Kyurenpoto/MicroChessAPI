# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.modeldto import ModelRequest, ModelResponse
from domain.microchess import MICRO_STARTING_FEN, MicroBoardStatus
from domain.model import ChessModel

from test.constant import MICRO_FIRST_MOVE_FEN, MICRO_FIRST_MOVE_SAN, MICRO_FIRST_NEXT_MOVE_LIST

def test_act() -> None:
    model: ChessModel = ChessModel()
    request: ModelRequest = ModelRequest(fens=[MICRO_STARTING_FEN], sans=[MICRO_FIRST_MOVE_SAN])
    response: ModelResponse = model.act(request)
    
    assert response == ModelResponse(
        fens=[MICRO_FIRST_MOVE_FEN],
        statuses=[MicroBoardStatus.NONE],
        legal_moves=[MICRO_FIRST_NEXT_MOVE_LIST])