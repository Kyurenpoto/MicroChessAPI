# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Optional

import chess

EMPTY_BOARD = "\n".join(". . . . . . . .")

class RawBoardString:
    __slots__ = ["__fen"]

    __fen: str

    def __init__(self, fen: str):
        self.__fen = fen

    def __str__(self) -> str:
        try:
            return str(chess.Board(str(self.__fen)))
        except:
            return EMPTY_BOARD
