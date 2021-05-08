# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, List

import chess

BLACK_CASTLING_UCI: Final[str] = "e8g8"
WHITE_CASTLING_UCI: Final[str] = "h4f4"
CASTLING_SAN: Final[str] = "O-O"


class RawLegalMoves:
    __slots__ = ["__fen"]

    __fen: str

    def __init__(self, fen: str):
        self.__fen = fen

    def value(self) -> List[str]:
        return [
            CASTLING_SAN if move.uci() == BLACK_CASTLING_UCI else move.uci()
            for move in chess.Board(self.__fen).legal_moves
        ]
