# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.implementation.legalsan import LegalSANs
from domain.implementation.validmicrofen import (
    MICRO_BLACK_CASTLABLE_FEN,
    MICRO_CHECKMATE_FEN,
    MICRO_STALEMATE_FEN,
    MICRO_STARTING_FEN,
    MICRO_WHITE_CASTLABLE_FEN,
)


def test_normal() -> None:
    assert LegalSANs.from_FEN(MICRO_STARTING_FEN) == LegalSANs.initial()


def test_checkmate() -> None:
    assert LegalSANs.from_FEN(MICRO_CHECKMATE_FEN) == []


def test_stalemate() -> None:
    assert LegalSANs.from_FEN(MICRO_STALEMATE_FEN) == []


def test_black_castlable() -> None:
    assert LegalSANs.from_FEN(MICRO_BLACK_CASTLABLE_FEN) == LegalSANs.black_castable()


def test_white_castlable() -> None:
    assert LegalSANs.from_FEN(MICRO_WHITE_CASTLABLE_FEN) == LegalSANs.white_castable()
