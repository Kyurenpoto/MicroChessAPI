# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, Set

from .basictype import SAN
from .mappable import Mappable

MICRO_CASTLING_SAN: Final[SAN] = SAN("O-O")
MICRO_FIRST_MOVE_SAN: Final[SAN] = SAN("h5h6")
MICRO_SECOND_MOVE_SAN: Final[SAN] = SAN("e7e6")
MICRO_KING_SIDE_MOVE_SAN: Final[SAN] = SAN("h4g4")
MICRO_BLACK_DOUBLE_MOVE_SAN: Final[SAN] = SAN("e7e5")

PROMOTIONABLE_PIECES: Final[str] = "QqRrBbNn"
VALID_SQUARES: Final[Set[str]] = set([i + j for j in "45678" for i in "efgh"])


class LengthValidSAN:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> SAN:
        if not (4 <= len(self.__san) <= 5):
            raise RuntimeError("The length of the normal SAN string must be 4 or 5")

        return self.__san


class FromSquareValidSAN:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> SAN:
        if self.__san[:2] not in VALID_SQUARES:
            raise RuntimeError("Only files e to h and ranks 4 to 8 are used in MicroChess")

        return self.__san


class ToSquareValidSAN:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> SAN:
        if self.__san[2:4] not in VALID_SQUARES:
            raise RuntimeError("Only files e to h and ranks 4 to 8 are used in MicroChess")

        return self.__san


class PromotionValidSAN:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> SAN:
        if len(self.__san) == 5 and self.__san[4] not in PROMOTIONABLE_PIECES:
            raise RuntimeError("Pawn can only promote to Queen, Rook, Knight, and Bishop")

        return self.__san


class ValidMicroSAN:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> SAN:
        if self.__san == MICRO_CASTLING_SAN:
            return self.__san

        return (
            Mappable(LengthValidSAN(self.__san).value())
            .mapped(lambda x: FromSquareValidSAN(x).value())
            .mapped(lambda x: ToSquareValidSAN(x).value())
            .mapped(lambda x: PromotionValidSAN(x).value())
            .value()
        )
