# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.implementation.legalsan import (
    MICRO_BLACK_CASTLABLE_LEGAL_MOVES,
    MICRO_FIRST_LEGAL_MOVES,
    MICRO_WHITE_CASTLABLE_LEGAL_MOVES,
    LegalSANs,
)
from domain.implementation.microboard import (
    MICRO_BLACK_CASTLABLE_FEN,
    MICRO_CHECKMATE_FEN,
    MICRO_FIRST_MOVE_FEN,
    MICRO_STALEMATE_FEN,
    MICRO_WHITE_CASTLABLE_FEN,
)


def test_normal() -> None:
    assert LegalSANs(MICRO_FIRST_MOVE_FEN).value() == MICRO_FIRST_LEGAL_MOVES


def test_checkmate() -> None:
    assert LegalSANs(MICRO_CHECKMATE_FEN).value() == []


def test_stalemate() -> None:
    assert LegalSANs(MICRO_STALEMATE_FEN).value() == []


def test_black_castlable() -> None:
    assert LegalSANs(MICRO_BLACK_CASTLABLE_FEN).value() == MICRO_BLACK_CASTLABLE_LEGAL_MOVES


def test_white_castlable() -> None:
    assert LegalSANs(MICRO_WHITE_CASTLABLE_FEN).value() == MICRO_WHITE_CASTLABLE_LEGAL_MOVES
