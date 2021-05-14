# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.modeldto import ModelNextFENRequest, ModelNextFENResponse
from domain.model import ChessModel, ChessModelBase


class ChessEnvironment:
    __slots__ = ["__model"]

    __model: ChessModelBase

    def __init__(self, model: ChessModelBase = ChessModel()):
        self.__model = model

    async def next_fen(self, request: ModelNextFENRequest) -> ModelNextFENResponse:
        return self.__model.next_fen(request)
