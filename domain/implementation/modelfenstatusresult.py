# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List, Tuple

from domain.implementation.microfen import MicroFEN
from domain.implementation.validmicrofen import ValidMicroFEN

from .basictype import FEN
from .fenstatus import FENStatus
from .legalsan import LegalSANs


class LegalMoves:
    __slots__ = ["__moved_boards"]

    __moved_boards: List[str]

    def __init__(self, moved_boards: List[str]):
        self.__moved_boards = moved_boards

    def value(self) -> List[List[str]]:
        return [[str(san) for san in LegalSANs(FEN(fen)).value()] for fen in self.__moved_boards]


class Statuses:
    __slots__ = ["__moved_boards", "__legal_moves"]

    __moved_boards: List[str]
    __legal_moves: List[List[str]]

    def __init__(self, moved_boards: List[str], legal_moves: List[List[str]]):
        self.__moved_boards = moved_boards
        self.__legal_moves = legal_moves

    def value(self) -> List[int]:
        return [
            int(FENStatus(FEN(fen), len(moves)).value().value)
            for fen, moves in zip(self.__moved_boards, self.__legal_moves)
        ]


class ModelFENStatusResult:
    __slots__ = ["__fens"]

    __fens: List[str]

    def __init__(self, fens: List[str]):
        self.__fens = fens

    def value(self) -> Tuple[List[List[str]], List[int]]:
        boards: List[str] = [
            str(ValidMicroFEN(MicroFEN(index, self.__fens)).value().fen()) for index in range(len(self.__fens))
        ]
        legal_moves: List[List[str]] = LegalMoves(boards).value()
        statuses: List[int] = Statuses(boards, legal_moves).value()

        return legal_moves, statuses
