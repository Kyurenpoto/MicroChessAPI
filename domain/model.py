# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from abc import ABCMeta, abstractmethod
from typing import List

from domain.implementation.boardstring import FEN
from domain.microchess import MicroBoardStatus, MovedMicroBoard
from domain.dto.modeldto import ModelRequest, ModelResponse

from test.constant import MICRO_FIRST_MOVE_FEN, MICRO_FIRST_NEXT_MOVE_LIST

class ChessModelBase(metaclass=ABCMeta):
    @abstractmethod
    def act(self, request: ModelRequest) -> ModelResponse:
        pass

class Fake(ChessModelBase):
    def act(self, request: ModelRequest) -> ModelResponse:
        return ModelResponse(
            fens=[MICRO_FIRST_MOVE_FEN],
            statuses=[MicroBoardStatus.NONE],
            legal_moves=[MICRO_FIRST_NEXT_MOVE_LIST])

class ChessModel(ChessModelBase):
    def act(self, request: ModelRequest) -> ModelResponse:
        moved: List[FEN] = [
            MovedMicroBoard(fen, san).value().fen()
            for fen, san in zip(request.fens, request.sans)]
        
        return ModelResponse(
            fens=moved,
            statuses=[MicroBoardStatus.NONE],
            legal_moves=[MICRO_FIRST_NEXT_MOVE_LIST])
