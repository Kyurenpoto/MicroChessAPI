# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Optional, cast

import chess

from .extendtype import Nullable
from .boardstring import FEN, BoardString, ValidMicroBoardString

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

class BoardPartValidMicroFen:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[FEN]:
        return Nullable(CreatedBoard(self.__fen).value()).op(
            lambda x: BoardString(cast(chess.Board, x))).op(
            lambda x: ValidMicroBoardString(x).value()).op(
            lambda x: None if x is None else self.__fen).value()

class CastlingPartValidMicroFen:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[FEN]:
        castling: str = self.__fen.split(" ")[2]
        return None if ("Q" in castling or "q" in castling) else self.__fen

class EnpassantPartValidMicroFen:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[FEN]:
        return self.__fen if self.__fen.split(" ")[3] == "-" else None

class ValidMicroFen:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[FEN]:
        return Nullable(BoardPartValidMicroFen(self.__fen).value()).op(
            lambda x: CastlingPartValidMicroFen(cast(FEN, x)).value()).op(
            lambda x: EnpassantPartValidMicroFen(cast(FEN, x)).value()).value()
