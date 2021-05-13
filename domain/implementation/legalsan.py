# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, List, Optional

from infra.rawlegalmoves import CASTLING_SAN, RawLegalMoves

from .basictype import FEN, SAN
from .microfen import MirroredMicroFEN
from .microsan import MicroSAN
from .validmicrosan import MICRO_BLACK_DOUBLE_MOVE_SAN, ValidMicroSAN


class LegalSAN:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> Optional[SAN]:
        try:
            return ValidMicroSAN(MicroSAN(0, [self.__san])).value().value()
        except RuntimeError:
            return None


MICRO_MAX_LEGAL_MOVES: Final[int] = 34
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
MICRO_BLACK_CASTLABLE_LEGAL_MOVES: Final[List[SAN]] = [
    SAN("O-O"),
    SAN("e7e6"),
    SAN("e8f7"),
    SAN("e8f8"),
    SAN("h8f8"),
    SAN("h8g8"),
    SAN("h8h5"),
    SAN("h8h6"),
    SAN("h8h7"),
]
MICRO_WHITE_CASTLABLE_LEGAL_MOVES: Final[List[SAN]] = [
    SAN("O-O"),
    SAN("e4e5"),
    SAN("e4e6"),
    SAN("e4e7"),
    SAN("e4f4"),
    SAN("e4g4"),
    SAN("h4g4"),
    SAN("h4g5"),
    SAN("h5h6"),
]


class CorrectedRawLegalMoves:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> List[str]:
        if self.__fen.split(" ")[1] == "w":
            return RawLegalMoves(self.__fen).value() + (
                [CASTLING_SAN] if CASTLING_SAN in RawLegalMoves(MirroredMicroFEN(self.__fen).value()).value() else []
            )
        else:
            return RawLegalMoves(self.__fen).value()


class LegalSANs:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> List[SAN]:
        return sorted(
            filter(
                lambda x: x != MICRO_BLACK_DOUBLE_MOVE_SAN,
                filter(
                    lambda x: LegalSAN(x).value() is not None,
                    map(lambda x: SAN(x), CorrectedRawLegalMoves(self.__fen).value()),
                ),
            )
        )
