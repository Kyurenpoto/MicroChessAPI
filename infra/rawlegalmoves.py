# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List

import chess


class RawLegalMoves:
    __slots__ = ["__fen"]

    __fen: str

    def __init__(self, fen: str):
        self.__fen = fen

    def value(self) -> List[str]:
        board: chess.Board = chess.Board(self.__fen)

        return [move.uci() for move in board.legal_moves]
