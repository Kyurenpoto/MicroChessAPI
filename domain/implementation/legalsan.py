# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, List

from infra.rawlegalmoves import RawLegalMoves

from .boardstring import FEN
from .microsan import SAN, ValidMicroSAN

MICRO_FIRST_LEGAL_MOVES: Final[List[SAN]] = [
    SAN("e7e6"),
    SAN("e8f7"),
    SAN("f8e6"),
    SAN("f8g6"),
    SAN("f8h7"),
    SAN("g8e6"),
    SAN("g8f7"),
    SAN("g8h7"),
    SAN("h8h6"),
    SAN("h8h7"),
]


class LegalSAN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> List[SAN]:
        legal_moves: List[SAN] = []
        for san in RawLegalMoves(self.__fen).value():
            valid = ValidMicroSAN(SAN(san)).value()
            if valid is not None and valid != "e7e5":
                legal_moves += [valid]

        return sorted(legal_moves)
