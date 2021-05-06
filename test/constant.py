# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, List

from domain.implementation.boardstring import FEN
from domain.microchess import SAN

MICRO_K_FEN: Final[FEN] = FEN("4k3/8/8/8/7K/8/8/8 w Kk - 0 1")
MICRO_FIRST_MOVE_FEN: Final[FEN] = FEN("4knbr/4p3/7P/8/4RBNK/8/8/8 b Kk - 0 1")
MICRO_FIRST_MOVE_SAN: Final[SAN] = SAN("h5h6")
MICRO_FIRST_NEXT_MOVE_LIST: Final[List[SAN]] = [
    SAN("bg8e6"), SAN("bg8f7"), SAN("bg8h7"),
    SAN("e7e6"),
    SAN("ke8f7"),
    SAN("nf8e6"), SAN("nf8g6"),
    SAN("rh8e6"), SAN("rh8e7")]
