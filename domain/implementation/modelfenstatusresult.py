# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import NamedTuple

from domain.implementation.microfen import MicroFEN
from domain.implementation.validmicrofen import ValidMicroFEN

from .basictype import FEN
from .legalsan import LegalSANs
from .microboardstatus import MicroBoardStatus


class LegalMoves(NamedTuple):
    moved_boards: list[str]

    def value(self) -> list[list[str]]:
        return [[str(san) for san in LegalSANs.from_FEN(FEN(fen))] for fen in self.moved_boards]


class Statuses(NamedTuple):
    moved_boards: list[str]
    legal_moves: list[list[str]]

    def value(self) -> list[int]:
        return [
            int(MicroBoardStatus.from_fen_with_legal_moves(FEN(fen), len(moves)).value)
            for fen, moves in zip(self.moved_boards, self.legal_moves)
        ]


class ModelFENStatusResult(NamedTuple):
    fens: list[str]

    def value(self) -> tuple[list[list[str]], list[int]]:
        boards: list[str] = [
            str(ValidMicroFEN(MicroFEN(index, self.fens)).value().fen()) for index in range(len(self.fens))
        ]
        legal_moves: list[list[str]] = LegalMoves(boards).value()
        statuses: list[int] = Statuses(boards, legal_moves).value()

        return legal_moves, statuses
