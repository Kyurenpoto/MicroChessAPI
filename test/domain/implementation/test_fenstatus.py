# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

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
