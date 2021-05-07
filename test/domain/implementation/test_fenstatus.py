# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.implementation.fenstatus import FENStatus
from domain.implementation.legalsan import MICRO_FIRST_LEGAL_MOVES
from domain.implementation.microboard import MICRO_CHECKMATE_FEN, MICRO_STALEMATE_FEN, MICRO_STARTING_FEN
from domain.implementation.microboardstatus import MicroBoardStatus


def test_none() -> None:
    assert MicroBoardStatus.NONE == FENStatus(MICRO_STARTING_FEN, len(MICRO_FIRST_LEGAL_MOVES)).value()


def test_checkmate() -> None:
    assert MicroBoardStatus.CHECKMATE == FENStatus(MICRO_CHECKMATE_FEN, 0).value()


def test_stalemate() -> None:
    assert MicroBoardStatus.STALEMATE == FENStatus(MICRO_STALEMATE_FEN, 0).value()
