# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Optional

import chess

class RawCheckedBoard:
    __slots__ = ["__fen"]

    __fen: str

    def __init__(self, fen: str):
        self.__fen = fen

    def value(self) -> Optional[str]:
        board: chess.Board = chess.Board(self.__fen)

        return self.__fen if board.is_check() else None
