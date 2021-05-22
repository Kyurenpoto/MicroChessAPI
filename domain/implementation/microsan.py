# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from domain.error.microsanerror import InvalidFromSquare, InvalidLength, InvalidPromotion, InvalidToSquare
from domain.implementation.mappable import Mappable
from domain.implementation.square import Square

from .basictype import SAN


class MicroSAN:
    __slots__ = ["__index", "__sans", "__san"]

    __index: int
    __sans: list[str]
    __san: SAN

    def __init__(self, index: int, sans: list[str]):
        self.__index = index
        self.__sans = sans
        self.__san = SAN("")

    def san(self) -> SAN:
        if self.__san == SAN(""):
            self.__san = SAN(self.__sans[self.__index])

        return self.__san

    def index(self) -> int:
        return self.__index

    def sans(self) -> list[str]:
        return self.__sans


class LengthValidSAN(MicroSAN):
    @classmethod
    def from_MicroSAN(cls, san: MicroSAN) -> LengthValidSAN:
        if not (4 <= len(san.san()) <= 5):
            raise RuntimeError(InvalidLength.from_index_with_SANs(san.index(), san.sans()))

        return LengthValidSAN(san.index(), san.sans())


class FromSquareValidSAN(MicroSAN):
    @classmethod
    def from_MicroSAN(cls, san: MicroSAN) -> FromSquareValidSAN:
        if san.san()[:2] not in Square.valid_set():
            raise RuntimeError(InvalidFromSquare.from_index_with_SANs(san.index(), san.sans()))

        return FromSquareValidSAN(san.index(), san.sans())


class ToSquareValidSAN(MicroSAN):
    @classmethod
    def from_MicroSAN(cls, san: MicroSAN) -> ToSquareValidSAN:
        if san.san()[2:4] not in Square.valid_set():
            raise RuntimeError(InvalidToSquare.from_index_with_SANs(san.index(), san.sans()))

        return ToSquareValidSAN(san.index(), san.sans())


class PromotionValidSAN(MicroSAN):
    @classmethod
    def from_MicroSAN(cls, san: MicroSAN) -> PromotionValidSAN:
        if len(san.san()) == 5 and san.san()[4] not in "QqRrBbNn":
            raise RuntimeError(InvalidPromotion.from_index_with_SANs(san.index(), san.sans()))

        return PromotionValidSAN(san.index(), san.sans())


class ValidMicroSAN(MicroSAN):
    @classmethod
    def from_MicroSAN(cls, san: MicroSAN) -> ValidMicroSAN:
        valid: MicroSAN = (
            san
            if san.san() == SAN.castling()
            else (
                Mappable(LengthValidSAN.from_MicroSAN(san))
                .mapped(lambda x: FromSquareValidSAN.from_MicroSAN(x))
                .mapped(lambda x: ToSquareValidSAN.from_MicroSAN(x))
                .mapped(lambda x: PromotionValidSAN.from_MicroSAN(x))
                .value()
            )
        )

        return ValidMicroSAN(valid.index(), valid.sans())
