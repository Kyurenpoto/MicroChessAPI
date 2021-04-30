# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations
from enum import Enum
from typing import Optional, Final, cast

import chess

from .implementation.extendtype import Nullable
from .implementation.boardstring import FEN, BoardString, ValidMicroBoardString

class CreatedBoard:
    __slots__ = ["__board", "__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[chess.Board]:
        try:
            board: chess.Board = chess.Board(str(self.__fen))
            if BoardString(board).empty() is True:
                return None
        except:
            return None
        else:
            return board

MICRO_STARTING_FEN: Final[FEN] = FEN("4kbnr/4p3/8/7P/4RNBK/8/8/8 w Kk - 0 1")

class ValidMicroFen:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[FEN]:
        return Nullable(CreatedBoard(self.__fen).value()).op(
            lambda x: BoardString(cast(chess.Board, x))).op(
            lambda x: ValidMicroBoardString(x)).op(
            lambda x: x.value()).op(
            lambda x: None if x is None else self.__fen).value()

class MicroMove:
    def __init__(self, move: str):
        pass

class MicroBoardStatus(Enum):
    NONE = 0
    CHECKMATE = 1
    STALEMATE = 2

class MicroBoard:
    __slots__ = ["__fen", "__reversed_fen"]

    __fen: FEN
    __reversed_fen: FEN

    def __init__(self, fen: FEN = MICRO_STARTING_FEN):
        self.__fen = fen

    def fen(self) -> FEN:
        return self.__fen

    def move(self, move: MicroMove) -> MicroBoard:
        return MicroBoard()

class CreatedMicroBoard:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: str):
        self.__fen = FEN(fen)

    def value(self) -> Optional[MicroBoard]:
        return Nullable(ValidMicroFen(self.__fen).value()).op(
            lambda x: (None if x is None else MicroBoard(x))).value()
