# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, List

from domain.implementation.boardstring import FEN
from domain.microchess import SAN

MICRO_K_FEN: Final[FEN] = FEN("4k3/8/8/8/7K/8/8/8 w Kk - 0 1")
MICRO_FIRST_MOVE_FEN: Final[FEN] = FEN("4knbr/4p3/7P/8/4RBNK/8/8/8 b Kk - 0 1")
MICRO_FIRST_MOVE_SAN: Final[SAN] = SAN("f8")
MICRO_FIRST_NEXT_MOVE_LIST: Final[List[SAN]] = [
    SAN("bf5"), SAN("bg6"), SAN("bg8"),
    SAN("f5"),
    SAN("kg6"),
    SAN("nf5"), SAN("nf7"),
    SAN("rf5"), SAN("rg5")]
