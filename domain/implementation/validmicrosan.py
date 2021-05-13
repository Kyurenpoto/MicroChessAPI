# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, Set

from domain.error.microsanerror import InvalidFromSquare, InvalidLength, InvalidPromotion, InvalidToSquare

from .basictype import SAN
from .mappable import Mappable
from .microsan import MicroSAN

MICRO_CASTLING_SAN: Final[SAN] = SAN("O-O")
MICRO_FIRST_MOVE_SAN: Final[SAN] = SAN("h5h6")
MICRO_SECOND_MOVE_SAN: Final[SAN] = SAN("e7e6")
MICRO_KING_SIDE_MOVE_SAN: Final[SAN] = SAN("h4g4")
MICRO_BLACK_DOUBLE_MOVE_SAN: Final[SAN] = SAN("e7e5")

PROMOTIONABLE_PIECES: Final[str] = "QqRrBbNn"
VALID_SQUARES: Final[Set[str]] = set([i + j for j in "45678" for i in "efgh"])


class LengthValidSAN:
    __slots__ = ["__san"]

    __san: MicroSAN

    def __init__(self, san: MicroSAN):
        self.__san = san

    def value(self) -> MicroSAN:
        if not (4 <= len(self.__san.value()) <= 5):
            raise RuntimeError(InvalidLength(self.__san.index(), self.__san.sans()).value())

        return self.__san


class FromSquareValidSAN:
    __slots__ = ["__san"]

    __san: MicroSAN

    def __init__(self, san: MicroSAN):
        self.__san = san

    def value(self) -> MicroSAN:
        if self.__san.value()[:2] not in VALID_SQUARES:
            raise RuntimeError(InvalidFromSquare(self.__san.index(), self.__san.sans()).value())

        return self.__san


class ToSquareValidSAN:
    __slots__ = ["__san"]

    __san: MicroSAN

    def __init__(self, san: MicroSAN):
        self.__san = san

    def value(self) -> MicroSAN:
        if self.__san.value()[2:4] not in VALID_SQUARES:
            raise RuntimeError(InvalidToSquare(self.__san.index(), self.__san.sans()).value())

        return self.__san


class PromotionValidSAN:
    __slots__ = ["__san"]

    __san: MicroSAN

    def __init__(self, san: MicroSAN):
        self.__san = san

    def value(self) -> MicroSAN:
        if len(self.__san.value()) == 5 and self.__san.value()[4] not in PROMOTIONABLE_PIECES:
            raise RuntimeError(InvalidPromotion(self.__san.index(), self.__san.sans()).value())

        return self.__san


class ValidMicroSAN:
    __slots__ = ["__san"]

    __san: MicroSAN

    def __init__(self, san: MicroSAN):
        self.__san = san

    def value(self) -> MicroSAN:
        return (
            self.__san
            if self.__san.value() == MICRO_CASTLING_SAN
            else (
                Mappable(LengthValidSAN(self.__san).value())
                .mapped(lambda x: FromSquareValidSAN(x).value())
                .mapped(lambda x: ToSquareValidSAN(x).value())
                .mapped(lambda x: PromotionValidSAN(x).value())
                .value()
            )
        )
