# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod

from domain.dto.modeldto import ModelRequest, ModelResponse
from domain.implementation.legalsan import MICRO_FIRST_LEGAL_MOVES
from domain.implementation.microboard import MICRO_FIRST_MOVE_FEN
from domain.implementation.modelactresult import ModelActResult


class ChessModelBase(metaclass=ABCMeta):
    @abstractmethod
    def act(self, request: ModelRequest) -> ModelResponse:
        pass


class Fake(ChessModelBase):
    def act(self, request: ModelRequest) -> ModelResponse:
        return ModelResponse(
            fens=[MICRO_FIRST_MOVE_FEN],
            statuses=[0],
            legal_moves=[MICRO_FIRST_LEGAL_MOVES],
        )


class ChessModel(ChessModelBase):
    def act(self, request: ModelRequest) -> ModelResponse:
        if len(request.fens) == 0:
            raise RuntimeError("At least one FEN must be entered")
        if len(request.sans) == 0:
            raise RuntimeError("At least one SAN must be entered")
        if len(request.fens) != len(request.sans):
            raise RuntimeError("The number of FENs and the number of SANs do not matched")

        moved_boards, legal_moves, statuses = ModelActResult(request.fens, request.sans).value()

        return ModelResponse(fens=moved_boards, statuses=statuses, legal_moves=legal_moves)
