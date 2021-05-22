# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import NamedTuple

from domain.dto.modeldto import ModelFENStatusRequest, ModelNextFENRequest
from domain.error.dtoerror import EmptyFENs, EmptySANs, NotMatchedNumberFENsSANs
from domain.implementation.mappable import Mappable


class NotEmptyFENsModelNextFENRequest(NamedTuple):
    request: ModelNextFENRequest

    def value(self) -> ModelNextFENRequest:
        if len(self.request.fens) == 0:
            raise RuntimeError(EmptyFENs.from_FENs(self.request.fens))

        return self.request


class NotEmptySANsModelNextFENRequest(NamedTuple):
    request: ModelNextFENRequest

    def value(self) -> ModelNextFENRequest:
        if len(self.request.sans) == 0:
            raise RuntimeError(EmptySANs.from_SANs(self.request.sans))

        return self.request


class FENsSANsNumberMatchtedModelNextFENRequest(NamedTuple):
    request: ModelNextFENRequest

    def value(self) -> ModelNextFENRequest:
        if len(self.request.fens) != len(self.request.sans):
            raise RuntimeError(NotMatchedNumberFENsSANs.from_FENs_SANs(self.request.fens, self.request.sans))

        return self.request


class ValidModelNextFENRequest(NamedTuple):
    request: ModelNextFENRequest

    def value(self) -> ModelNextFENRequest:
        return (
            Mappable(NotEmptyFENsModelNextFENRequest(self.request).value())
            .mapped(lambda x: NotEmptySANsModelNextFENRequest(x).value())
            .mapped(lambda x: FENsSANsNumberMatchtedModelNextFENRequest(x).value())
            .value()
        )


class NotEmptyFENsModelFENStatusRequest(NamedTuple):
    request: ModelFENStatusRequest

    def value(self) -> ModelFENStatusRequest:
        if len(self.request.fens) == 0:
            raise RuntimeError(EmptyFENs.from_FENs(self.request.fens))

        return self.request


class ValidModelFENStatusRequest(NamedTuple):
    request: ModelFENStatusRequest

    def value(self) -> ModelFENStatusRequest:
        return NotEmptyFENsModelFENStatusRequest(self.request).value()
