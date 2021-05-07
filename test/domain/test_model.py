# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.modeldto import ModelRequest, ModelResponse
from domain.implementation.legalsan import MICRO_FIRST_LEGAL_MOVES
from domain.implementation.microboard import MICRO_FIRST_MOVE_FEN, MICRO_STARTING_FEN
from domain.implementation.microsan import MICRO_FIRST_MOVE_SAN
from domain.model import ChessModel


def test_act() -> None:
    model: ChessModel = ChessModel()
    request: ModelRequest = ModelRequest(fens=[MICRO_STARTING_FEN], sans=[MICRO_FIRST_MOVE_SAN])
    response: ModelResponse = model.act(request)

    assert response == ModelResponse(fens=[MICRO_FIRST_MOVE_FEN], statuses=[0], legal_moves=[MICRO_FIRST_LEGAL_MOVES])
