# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.implementation.microfen import MicroFEN
from domain.implementation.validmicrofen import ValidMicroFEN

from .basictype import FEN
from .fenstatus import FENStatus
from .legalsan import LegalSANs


class LegalMoves:
    __slots__ = ["__moved_boards"]

    __moved_boards: list[str]

    def __init__(self, moved_boards: list[str]):
        self.__moved_boards = moved_boards

    def value(self) -> list[list[str]]:
        return [[str(san) for san in LegalSANs(FEN(fen)).value()] for fen in self.__moved_boards]


class Statuses:
    __slots__ = ["__moved_boards", "__legal_moves"]

    __moved_boards: list[str]
    __legal_moves: list[list[str]]

    def __init__(self, moved_boards: list[str], legal_moves: list[list[str]]):
        self.__moved_boards = moved_boards
        self.__legal_moves = legal_moves

    def value(self) -> list[int]:
        return [
            int(FENStatus(FEN(fen), len(moves)).value().value)
            for fen, moves in zip(self.__moved_boards, self.__legal_moves)
        ]


class ModelFENStatusResult:
    __slots__ = ["__fens"]

    __fens: list[str]

    def __init__(self, fens: list[str]):
        self.__fens = fens

    def value(self) -> tuple[list[list[str]], list[int]]:
        boards: list[str] = [
            str(ValidMicroFEN(MicroFEN(index, self.__fens)).value().fen()) for index in range(len(self.__fens))
        ]
        legal_moves: list[list[str]] = LegalMoves(boards).value()
        statuses: list[int] = Statuses(boards, legal_moves).value()

        return legal_moves, statuses
