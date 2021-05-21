# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import NamedTuple, Optional

import chess


class RawCheckedFEN(NamedTuple):
    fen: str

    def value(self) -> Optional[str]:
        board: chess.Board = chess.Board(self.fen)

        return self.fen if board.is_check() else None
