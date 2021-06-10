# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from typing import NamedTuple

from src.domain.implementation.basictype import FEN
from src.domain.implementation.legalsan import LegalSANs
from src.domain.implementation.microboardstatus import MicroBoardStatus
from src.domain.implementation.microfen import MicroFEN
from src.domain.implementation.validmicrofen import ValidMicroFEN


class LegalMoves(list[list[str]]):
    @classmethod
    def from_valid_FENs(cls, fens: list[str]) -> LegalMoves:
        return LegalMoves([[str(san) for san in LegalSANs.from_FEN(FEN(fen))] for fen in fens])

    @classmethod
    def from_FENs(cls, fens: list[str]) -> LegalMoves:
        return LegalMoves.from_valid_FENs(
            [
                str(ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(index, fens)).fen)
                for index in range(len(fens))
            ]
        )


class Statuses(list[int]):
    @classmethod
    def from_FENs_with_legal_moves(cls, fens: list[str], legal_moves: list[list[str]]) -> Statuses:
        return Statuses(
            [
                int(MicroBoardStatus.from_fen_with_legal_moves(FEN(fen), len(moves)).value)
                for fen, moves in zip(fens, legal_moves)
            ]
        )


class ModelFENStatusResult(NamedTuple):
    legal_moves: list[list[str]]
    statuses: list[int]

    @classmethod
    def from_FENs(cls, fens: list[str]) -> ModelFENStatusResult:
        legal_moves: list[list[str]] = LegalMoves.from_FENs(fens)
        statuses: list[int] = Statuses.from_FENs_with_legal_moves(fens, legal_moves)

        return ModelFENStatusResult(legal_moves, statuses)
