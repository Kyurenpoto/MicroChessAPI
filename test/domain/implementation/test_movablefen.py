# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from src.domain.implementation.basictype import FEN, SAN
from src.domain.implementation.movablefen import MovableFEN


def test_normal() -> None:
    assert MovableFEN(FEN.starting()).moved(SAN.first_move()) == FEN.first_move()


def test_black_castling() -> None:
    assert MovableFEN(FEN.black_castlable()).moved(SAN.castling()) == FEN.black_castled()


def test_white_castling() -> None:
    assert MovableFEN(FEN.white_castlable()).moved(SAN.castling()) == FEN.white_castled()


@pytest.mark.parametrize(
    "fen, mirrored",
    [
        (FEN.white_castlable(), FEN.black_castlable()),
        (FEN.black_castlable(), FEN.white_castlable()),
    ],
)
def test_mirror(fen: FEN, mirrored: FEN) -> None:
    assert MovableFEN(fen).mirrored() == mirrored
