# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Optional

import chess
from domain.implementation.microboardstatus import MicroBoardStatus


class RawFENOutcome:
    __slots__ = ["__fen"]

    __fen: str

    def __init__(self, fen: str):
        self.__fen = fen

    def value(self) -> MicroBoardStatus:
        outcome: Optional[chess.Outcome] = chess.Board(self.__fen).outcome()

        if outcome is None:
            return MicroBoardStatus.NONE
        if outcome.termination == chess.Termination.INSUFFICIENT_MATERIAL:
            return MicroBoardStatus.INSUFFICIENT_MATERIAL
        if outcome.termination == chess.Termination.FIFTY_MOVES:
            return MicroBoardStatus.FIFTY_MOVES

        return MicroBoardStatus.NONE
