# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod

from domain.dto.modeldto import ModelRequest, ModelResponse
from domain.implementation.modelactresult import ModelActResult

from test.constant import MICRO_FIRST_MOVE_FEN, MICRO_FIRST_LEGAL_MOVES

class ChessModelBase(metaclass=ABCMeta):
    @abstractmethod
    def act(self, request: ModelRequest) -> ModelResponse:
        pass

class Fake(ChessModelBase):
    def act(self, request: ModelRequest) -> ModelResponse:
        return ModelResponse(
            fens=[MICRO_FIRST_MOVE_FEN],
            statuses=[0],
            legal_moves=[MICRO_FIRST_LEGAL_MOVES])

class ChessModel(ChessModelBase):
    def act(self, request: ModelRequest) -> ModelResponse:
        moved, legal_moves, statuses = ModelActResult(request.fens, request.sans).value()
        
        return ModelResponse(
            fens=moved,
            statuses=statuses,
            legal_moves=legal_moves)
