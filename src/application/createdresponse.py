# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import NamedTuple, Union

from dependency_injector import providers
from src.config import container
from src.domain.dto.modeldto import (
    ModelAPIInfo,
    ModelFENStatusRequest,
    ModelFENStatusResponse,
    ModelNextFENRequest,
    ModelNextFENResponse,
)
from src.domain.implementation.validmodeldto import ValidModelFENStatusRequest, ValidModelNextFENRequest
from src.domain.model import MicroChessModel


class FENStatusRequestData(NamedTuple):
    request: ModelFENStatusRequest
    name: str = "fen-status"
    method: str = "post"


class NextFENRequestData(NamedTuple):
    request: ModelNextFENRequest
    name: str = "next-fen"
    method: str = "post"


class ICreatedResponse(metaclass=ABCMeta):
    @abstractmethod
    def created(self) -> Union[ModelFENStatusResponse, ModelNextFENResponse]:
        pass


class CreatedFENStatusResponse(FENStatusRequestData, ICreatedResponse):
    def created(self) -> Union[ModelFENStatusResponse, ModelNextFENResponse]:
        container.api_info.override(providers.Factory(ModelAPIInfo, name="fen-status", method="post"))

        return MicroChessModel().fen_status(ValidModelFENStatusRequest.from_request(self.request))


class CreatedNextFENResponse(NextFENRequestData, ICreatedResponse):
    def created(self) -> Union[ModelFENStatusResponse, ModelNextFENResponse]:
        container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

        return MicroChessModel().next_fen(ValidModelNextFENRequest.from_request(self.request))
