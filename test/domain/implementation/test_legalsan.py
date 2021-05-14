# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.implementation.legalsan import (
    MICRO_BLACK_CASTLABLE_LEGAL_MOVES,
    MICRO_INITIAL_LEGAL_MOVES,
    MICRO_WHITE_CASTLABLE_LEGAL_MOVES,
    LegalSANs,
)
from domain.implementation.movedfen import (
    MICRO_BLACK_CASTLABLE_FEN,
    MICRO_CHECKMATE_FEN,
    MICRO_STALEMATE_FEN,
    MICRO_STARTING_FEN,
    MICRO_WHITE_CASTLABLE_FEN,
)


def test_normal() -> None:
    assert LegalSANs(MICRO_STARTING_FEN).value() == MICRO_INITIAL_LEGAL_MOVES


def test_checkmate() -> None:
    assert LegalSANs(MICRO_CHECKMATE_FEN).value() == []


def test_stalemate() -> None:
    assert LegalSANs(MICRO_STALEMATE_FEN).value() == []


def test_black_castlable() -> None:
    assert LegalSANs(MICRO_BLACK_CASTLABLE_FEN).value() == MICRO_BLACK_CASTLABLE_LEGAL_MOVES


def test_white_castlable() -> None:
    assert LegalSANs(MICRO_WHITE_CASTLABLE_FEN).value() == MICRO_WHITE_CASTLABLE_LEGAL_MOVES
