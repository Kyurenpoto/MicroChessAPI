# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.error.dtoerror import EmptyFENs, EmptySANs, NotMatchedNumberFENsSANs
from domain.implementation.mappable import Mappable

from .modeldto import ModelRequest


class NotEmptyFENsModelRequest:
    __slots__ = ["__request"]

    __request: ModelRequest

    def __init__(self, request: ModelRequest):
        self.__request = request

    def value(self) -> ModelRequest:
        if len(self.__request.fens) == 0:
            raise RuntimeError(EmptyFENs(self.__request.fens).value())

        return self.__request


class NotEmptySANsModelRequest:
    __slots__ = ["__request"]

    __request: ModelRequest

    def __init__(self, request: ModelRequest):
        self.__request = request

    def value(self) -> ModelRequest:
        if len(self.__request.sans) == 0:
            raise RuntimeError(EmptySANs(self.__request.sans).value())

        return self.__request


class FENsSANsNumberMatchtedModelRequest:
    __slots__ = ["__request"]

    __request: ModelRequest

    def __init__(self, request: ModelRequest):
        self.__request = request

    def value(self) -> ModelRequest:
        if len(self.__request.fens) != len(self.__request.sans):
            raise RuntimeError(NotMatchedNumberFENsSANs(self.__request.fens, self.__request.sans).value())

        return self.__request


class ValidModelRequest:
    __slots__ = ["__request"]

    __request: ModelRequest

    def __init__(self, request: ModelRequest):
        self.__request = request

    def value(self) -> ModelRequest:
        return (
            Mappable(self.__request)
            .mapped(lambda x: NotEmptyFENsModelRequest(x).value())
            .mapped(lambda x: NotEmptySANsModelRequest(x).value())
            .mapped(lambda x: FENsSANsNumberMatchtedModelRequest(x).value())
            .value()
        )
