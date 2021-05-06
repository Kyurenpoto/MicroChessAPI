# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List

import chess

class RawMovedFen:
    __slots__ = ["__fen", "__san"]

    __fen: str
    __san: str

    def __init__(self, fen: str, san: str):
        self.__fen = fen
        self.__san = san

    def __str__(self) -> str:
        origin: List[str] = self.__fen.split(" ")
        board: chess.Board = chess.Board(self.__fen)
        board.push_san(self.__san)
        
        moved: List[str] = board.fen().split(" ")
        if origin[2] != moved[2] and moved[1] == "b":
            return " ".join(moved[:2] + [origin[2]] + moved[3:])

        return " ".join(moved)
