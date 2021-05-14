# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.modeldto import ModelNextFENRequest
from domain.error.dtoerror import EmptyFENs, EmptySANs, NotMatchedNumberFENsSANs
from domain.implementation.mappable import Mappable


class NotEmptyFENsModelNextFENRequest:
    __slots__ = ["__request"]

    __request: ModelNextFENRequest

    def __init__(self, request: ModelNextFENRequest):
        self.__request = request

    def value(self) -> ModelNextFENRequest:
        if len(self.__request.fens) == 0:
            raise RuntimeError(EmptyFENs(self.__request.fens).value())

        return self.__request


class NotEmptySANsModelNextFENRequest:
    __slots__ = ["__request"]

    __request: ModelNextFENRequest

    def __init__(self, request: ModelNextFENRequest):
        self.__request = request

    def value(self) -> ModelNextFENRequest:
        if len(self.__request.sans) == 0:
            raise RuntimeError(EmptySANs(self.__request.sans).value())

        return self.__request


class FENsSANsNumberMatchtedModelNextFENRequest:
    __slots__ = ["__request"]

    __request: ModelNextFENRequest

    def __init__(self, request: ModelNextFENRequest):
        self.__request = request

    def value(self) -> ModelNextFENRequest:
        if len(self.__request.fens) != len(self.__request.sans):
            raise RuntimeError(NotMatchedNumberFENsSANs(self.__request.fens, self.__request.sans).value())

        return self.__request


class ValidModelNextFENRequest:
    __slots__ = ["__request"]

    __request: ModelNextFENRequest

    def __init__(self, request: ModelNextFENRequest):
        self.__request = request

    def value(self) -> ModelNextFENRequest:
        return (
            Mappable(NotEmptyFENsModelNextFENRequest(self.__request).value())
            .mapped(lambda x: NotEmptySANsModelNextFENRequest(x).value())
            .mapped(lambda x: FENsSANsNumberMatchtedModelNextFENRequest(x).value())
            .value()
        )
