# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import NamedTuple

from dependency_injector.wiring import Provide, inject
from src.config import Container
from src.domain.dto.modeldto import (
    ModelAPIInfo,
    ModelFENStatusRequest,
    ModelFENStatusResponse,
    ModelInternal,
    ModelNextFENRequest,
    ModelNextFENResponse,
)
from src.domain.implementation.basictype import FEN
from src.domain.implementation.legalsan import LegalSANs
from src.domain.implementation.modelfenstatusresult import ModelFENStatusResult
from src.domain.implementation.modelnextfenresult import ModelNextFENResult
from submodules.fastapi_haljson.src.halmodel import HALBase


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


class CreatedFENStatusResponse(NamedTuple):
    statuses: list[int]
    legal_moves: list[list[str]]

    @inject
    def created(
        self,
        internal_model: ModelInternal = Provide[Container.internal_model],
        api_info: ModelAPIInfo = Provide[Container.api_info],
    ) -> ModelFENStatusResponse:
        return ModelFENStatusResponse(
            links=HALBase.from_routes_with_requested(internal_model.routes, api_info.name, api_info.method).links,
            statuses=self.statuses,
            legal_moves=self.legal_moves,
        )


class CreatedNextFENResponse(NamedTuple):
    next_fens: list[str]

    @inject
    def created(
        self,
        internal_model: ModelInternal = Provide[Container.internal_model],
        api_info: ModelAPIInfo = Provide[Container.api_info],
    ) -> ModelNextFENResponse:
        return ModelNextFENResponse(
            links=HALBase.from_routes_with_requested(internal_model.routes, api_info.name, api_info.method).links,
            next_fens=self.next_fens,
        )


class MicroChessModel(ChessModelBase):
    def fen_status(self, request: ModelFENStatusRequest) -> ModelFENStatusResponse:
        legal_moves, statuses = ModelFENStatusResult.from_FENs(request.fens)

        return CreatedFENStatusResponse(statuses, legal_moves).created()

    def next_fen(self, request: ModelNextFENRequest) -> ModelNextFENResponse:
        moved_fens = ModelNextFENResult.from_FENs_SANs(request.fens, request.sans)

        return CreatedNextFENResponse(moved_fens).created()
