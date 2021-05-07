# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from infra.rawcheckedboard import RawCheckedBoard
from .boardstring import FEN
from .microboardstatus import MicroBoardStatus

class FENStatus:
    __slots__ = ["__fen", "__cnt_legal_moves"]

    __fen: FEN
    __cnt_legal_moves: int

    def __init__(self, fen: FEN, cnt_legal_moves: int):
        self.__fen = fen
        self.__cnt_legal_moves = cnt_legal_moves

    def value(self) -> MicroBoardStatus:
        if self.__cnt_legal_moves != 0:
            return MicroBoardStatus.NONE

        return (MicroBoardStatus.CHECKMATE
            if RawCheckedBoard(self.__fen).value()
            else MicroBoardStatus.STALEMATE)
