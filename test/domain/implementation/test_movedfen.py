# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.implementation.basictype import FEN, SAN
from domain.implementation.movedfen import MovedFEN


def test_normal() -> None:
    assert MovedFEN.from_FEN_SAN(FEN.starting(), SAN.first_move()) == FEN.first_move()


def test_black_castling() -> None:
    assert MovedFEN.from_FEN_SAN(FEN.black_castlable(), SAN.castling()) == FEN.black_castled()


def test_white_castling() -> None:
    assert MovedFEN.from_FEN_SAN(FEN.white_castlable(), SAN.castling()) == FEN.white_castled()
