# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import List

from .basictype import SAN
from .microsan import MICRO_CASTLING_SAN, MicroSAN, ValidMicroSAN


class MicroMove:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN = MICRO_CASTLING_SAN):
        self.__san = san

    def san(self) -> SAN:
        return self.__san


class CreatedMicroMove:
    __slots__ = ["__san"]

    __san: MicroSAN

    def __init__(self, san: MicroSAN):
        self.__san = san

    def value(self) -> MicroMove:
        return MicroMove(ValidMicroSAN(self.__san).value().value())
