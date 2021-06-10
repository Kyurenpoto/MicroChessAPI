# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod

from src.domain.dto.modeldto import (
    ModelFENStatusRequest,
    ModelFENStatusResponse,
    ModelNextFENRequest,
    ModelNextFENResponse,
)
from src.domain.implementation.basictype import FEN
from src.domain.implementation.legalsan import LegalSANs
from src.domain.implementation.modelfenstatusresult import ModelFENStatusResult
from src.domain.implementation.modelnextfenresult import ModelNextFENResult


class ChessModelBase(metaclass=ABCMeta):
    @abstractmethod
    def next_fen(self, request: ModelNextFENRequest) -> ModelNextFENResponse:
        pass

    @abstractmethod
    def fen_status(self, request: ModelFENStatusRequest) -> ModelFENStatusResponse:
        pass


class Fake(ChessModelBase):
    def next_fen(self, request: ModelNextFENRequest) -> ModelNextFENResponse:
        return ModelNextFENResponse(next_fens=[FEN.first_move()])

    def fen_status(self, request: ModelFENStatusRequest) -> ModelFENStatusResponse:
        return ModelFENStatusResponse(
            statuses=[1],
            legal_moves=[LegalSANs.initial()],
        )


class MicroChessModel(ChessModelBase):
    def next_fen(self, request: ModelNextFENRequest) -> ModelNextFENResponse:
        moved_fens = ModelNextFENResult.from_FENs_SANs(request.fens, request.sans)

        return ModelNextFENResponse(next_fens=moved_fens)

    def fen_status(self, request: ModelFENStatusRequest) -> ModelFENStatusResponse:
        legal_moves, statuses = ModelFENStatusResult.from_FENs(request.fens)

        return ModelFENStatusResponse(
            statuses=statuses,
            legal_moves=legal_moves,
        )
