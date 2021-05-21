# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.implementation.movedfen import MovedFEN
from domain.implementation.validmicrofen import (
    MICRO_BLACK_CASTLABLE_FEN,
    MICRO_BLACK_CASTLED_FEN,
    MICRO_FIRST_MOVE_FEN,
    MICRO_STARTING_FEN,
    MICRO_WHITE_CASTLABLE_FEN,
    MICRO_WHITE_CASTLED_FEN,
)
from domain.implementation.validmicrosan import MICRO_CASTLING_SAN, MICRO_FIRST_MOVE_SAN


def test_normal() -> None:
    assert MovedFEN.from_FEN_SAN(MICRO_STARTING_FEN, MICRO_FIRST_MOVE_SAN) == MICRO_FIRST_MOVE_FEN


def test_black_castling() -> None:
    assert MovedFEN.from_FEN_SAN(MICRO_BLACK_CASTLABLE_FEN, MICRO_CASTLING_SAN) == MICRO_BLACK_CASTLED_FEN


def test_white_castling() -> None:
    assert MovedFEN.from_FEN_SAN(MICRO_WHITE_CASTLABLE_FEN, MICRO_CASTLING_SAN) == MICRO_WHITE_CASTLED_FEN
