# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.implementation.basictype import FEN
from domain.implementation.movedfen import MovedFEN
from domain.implementation.validmicrosan import MICRO_CASTLING_SAN, MICRO_FIRST_MOVE_SAN


def test_normal() -> None:
    assert MovedFEN.from_FEN_SAN(FEN.starting(), MICRO_FIRST_MOVE_SAN) == FEN.first_move()


def test_black_castling() -> None:
    assert MovedFEN.from_FEN_SAN(FEN.black_castlable(), MICRO_CASTLING_SAN) == FEN.black_castled()


def test_white_castling() -> None:
    assert MovedFEN.from_FEN_SAN(FEN.white_castlable(), MICRO_CASTLING_SAN) == FEN.white_castled()
