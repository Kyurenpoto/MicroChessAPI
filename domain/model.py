# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod

from domain.dto.modeldto import ModelNextFENRequest, ModelNextFENResponse
from domain.implementation.legalsan import MICRO_FIRST_LEGAL_MOVES
from domain.implementation.modelnextfenresult import ModelNextFENResult
from domain.implementation.movedfen import MICRO_FIRST_MOVE_FEN


class ChessModelBase(metaclass=ABCMeta):
    @abstractmethod
    def next_fen(self, request: ModelNextFENRequest) -> ModelNextFENResponse:
        pass


class Fake(ChessModelBase):
    def next_fen(self, request: ModelNextFENRequest) -> ModelNextFENResponse:
        return ModelNextFENResponse(
            fens=[MICRO_FIRST_MOVE_FEN],
            statuses=[0],
            legal_moves=[MICRO_FIRST_LEGAL_MOVES],
        )


class ChessModel(ChessModelBase):
    def next_fen(self, request: ModelNextFENRequest) -> ModelNextFENResponse:
        moved_boards, legal_moves, statuses = ModelNextFENResult(request.fens, request.sans).value()

        return ModelNextFENResponse(fens=moved_boards, statuses=statuses, legal_moves=legal_moves)
