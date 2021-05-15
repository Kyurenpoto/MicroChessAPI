# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from enum import Enum, auto


class MicroBoardStatus(Enum):
    NONE = auto()
    CHECKMATE = auto()
    STALEMATE = auto()
    INSUFFICIENT_MATERIAL = auto()
    FIFTY_MOVES = auto()
