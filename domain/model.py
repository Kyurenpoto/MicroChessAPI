# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod

from domain.dto.modeldto import ModelFENStatusRequest, ModelFENStatusResponse, ModelNextFENRequest, ModelNextFENResponse
from domain.implementation.legalsan import MICRO_INITIAL_LEGAL_MOVES
from domain.implementation.modelfenstatusresult import ModelFENStatusResult
from domain.implementation.modelnextfenresult import ModelNextFENResult
from domain.implementation.movedfen import MICRO_FIRST_MOVE_FEN


class ChessModelBase(metaclass=ABCMeta):
    @abstractmethod
    def next_fen(self, request: ModelNextFENRequest) -> ModelNextFENResponse:
        pass

    @abstractmethod
    def fen_status(self, request: ModelFENStatusRequest) -> ModelFENStatusResponse:
        pass


class Fake(ChessModelBase):
    def next_fen(self, request: ModelNextFENRequest) -> ModelNextFENResponse:
        return ModelNextFENResponse(next_fens=[MICRO_FIRST_MOVE_FEN])

    def fen_status(self, request: ModelFENStatusRequest) -> ModelFENStatusResponse:
        return ModelFENStatusResponse(
            statuses=[1],
            legal_moves=[MICRO_INITIAL_LEGAL_MOVES],
        )


class ChessModel(ChessModelBase):
    def next_fen(self, request: ModelNextFENRequest) -> ModelNextFENResponse:
        moved_fens = ModelNextFENResult(request.fens, request.sans).value()

        return ModelNextFENResponse(next_fens=moved_fens)

    def fen_status(self, request: ModelFENStatusRequest) -> ModelFENStatusResponse:
        legal_moves, statuses = ModelFENStatusResult(request.fens).value()

        return ModelFENStatusResponse(
            statuses=statuses,
            legal_moves=legal_moves,
        )
