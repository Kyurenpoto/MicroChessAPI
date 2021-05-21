# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, NamedTuple

import chess

BLACK_CASTLING_UCI: Final[str] = "e8g8"
WHITE_CASTLING_UCI: Final[str] = "h4f4"
CASTLING_SAN: Final[str] = "O-O"


class RawLegalMoves(NamedTuple):
    fen: str

    def value(self) -> list[str]:
        return [
            CASTLING_SAN if move.uci() == BLACK_CASTLING_UCI else move.uci()
            for move in chess.Board(self.fen).legal_moves
        ]
