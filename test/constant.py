# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, List

from domain.implementation.boardstring import FEN
from domain.microchess import SAN

MICRO_FIRST_MOVE_FEN: Final[FEN] = FEN("4knbr/4p3/7P/8/4RBNK/8/8/8 b Kk - 0 1")
MICRO_FIRST_MOVE_SAN: Final[SAN] = SAN("h5h6")
MICRO_FIRST_LEGAL_MOVES: Final[List[SAN]] = [
    SAN("e7e6"),
    SAN("e8f7"),
    SAN("f8e6"), SAN("f8g6"), SAN("f8h7"),
    SAN("g8e6"), SAN("g8f7"), SAN("g8h7"),
    SAN("h8h6"), SAN("h8h7")]
