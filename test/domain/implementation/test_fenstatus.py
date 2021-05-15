# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from domain.implementation.basictype import FEN
from domain.implementation.fenstatus import FENStatus
from domain.implementation.legalsan import MICRO_INITIAL_LEGAL_MOVES
from domain.implementation.microboardstatus import MicroBoardStatus
from domain.implementation.movedfen import MICRO_CHECKMATE_FEN, MICRO_STALEMATE_FEN, MICRO_STARTING_FEN


def test_none() -> None:
    assert MicroBoardStatus.NONE == FENStatus(MICRO_STARTING_FEN, len(MICRO_INITIAL_LEGAL_MOVES)).value()


def test_checkmate() -> None:
    assert MicroBoardStatus.CHECKMATE == FENStatus(MICRO_CHECKMATE_FEN, 0).value()


def test_stalemate() -> None:
    assert MicroBoardStatus.STALEMATE == FENStatus(MICRO_STALEMATE_FEN, 0).value()


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
    assert MicroBoardStatus.INSUFFICIENT_MATERIAL == FENStatus(fen, 1).value()


def test_fifty_moves() -> None:
    assert MicroBoardStatus.FIFTY_MOVES == FENStatus(FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 50 51"), 1).value()
