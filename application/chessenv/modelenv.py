# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.modeldto import ModelRequest, ModelResponse
from domain.model import ChessModel, ChessModelBase


class ChessEnvironment:
    __slots__ = ["__model"]

    __model: ChessModelBase

    def __init__(self, model: ChessModelBase = ChessModel()):
        self.__model = model

    async def act(self, request: ModelRequest) -> ModelResponse:
        return self.__model.act(request)
