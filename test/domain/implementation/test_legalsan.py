# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.implementation.basictype import FEN
from domain.implementation.legalsan import LegalSANs


def test_normal() -> None:
    assert LegalSANs.from_FEN(FEN.starting()) == LegalSANs.initial()


def test_checkmate() -> None:
    assert LegalSANs.from_FEN(FEN.checkmate()) == []


def test_stalemate() -> None:
    assert LegalSANs.from_FEN(FEN.stalemate()) == []


def test_black_castlable() -> None:
    assert LegalSANs.from_FEN(FEN.black_castlable()) == LegalSANs.black_castable()


def test_white_castlable() -> None:
    assert LegalSANs.from_FEN(FEN.white_castlable()) == LegalSANs.white_castable()
