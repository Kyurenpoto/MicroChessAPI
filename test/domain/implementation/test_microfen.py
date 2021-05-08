# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.implementation.microboard import MICRO_BLACK_CASTLABLE_FEN, MICRO_WHITE_CASTLABLE_FEN
from domain.implementation.microfen import MirroredMicroFen


def test_castlable() -> None:
    assert MirroredMicroFen(MICRO_WHITE_CASTLABLE_FEN).value() == MICRO_BLACK_CASTLABLE_FEN
