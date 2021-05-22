# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from domain.implementation.basictype import FEN
from domain.implementation.legalsan import LegalSANs
from domain.implementation.microboardstatus import MicroBoardStatus


def test_none() -> None:
    assert MicroBoardStatus.from_fen_with_legal_moves(FEN.starting(), len(LegalSANs.initial())) == MicroBoardStatus.NONE


def test_checkmate() -> None:
    assert MicroBoardStatus.from_fen_with_legal_moves(FEN.checkmate(), 0) == MicroBoardStatus.CHECKMATE


def test_stalemate() -> None:
    assert MicroBoardStatus.from_fen_with_legal_moves(FEN.stalemate(), 0) == MicroBoardStatus.STALEMATE


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4k3/8/8/8/7K/8/8/8 w - - 0 1")),
        (FEN("4k3/8/8/8/6NK/8/8/8 w - - 0 1")),
        (FEN("4k3/8/8/8/5B1K/8/8/8 w - - 0 1")),
        (FEN("4k3/8/8/4B3/5B1K/8/8/8 w - - 0 1")),
    ],
)
def test_insufficient_material(fen: FEN) -> None:
    assert MicroBoardStatus.from_fen_with_legal_moves(fen, 1) == MicroBoardStatus.INSUFFICIENT_MATERIAL


def test_fifty_moves() -> None:
    assert (
        MicroBoardStatus.from_fen_with_legal_moves(FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 50 51"), 1)
        == MicroBoardStatus.FIFTY_MOVES
    )
