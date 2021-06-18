# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from typing import NamedTuple

from src.domain.error.microsanerror import InvalidFromSquare, InvalidLength, InvalidPromotion, InvalidToSquare
from src.domain.implementation.basictype import SAN
from src.domain.implementation.square import FromSquare, ToSquare


class MicroSAN(NamedTuple):
    index: int
    sans: list[str]
    san: SAN

    @classmethod
    def from_index_with_SANs(cls, index: int, sans: list[str]) -> MicroSAN:
        return MicroSAN(index, sans, SAN(sans[index]))


class ValidMicroSAN(MicroSAN):
    @classmethod
    def from_MicroSAN(cls, microsan: MicroSAN) -> ValidMicroSAN:
        return ValidMicroSAN._make(
            microsan
            if microsan.san == SAN.castling()
            else (ValidMicroSAN._make(microsan).valid_length().valid_from_square().valid_to_square().valid_promotion())
        )

    def valid_length(self) -> ValidMicroSAN:
        if not (4 <= len(self.san) <= 5):
            raise RuntimeError(InvalidLength.from_index_with_SANs(self.index, self.sans).created())

        return self

    def valid_from_square(self) -> ValidMicroSAN:
        if not FromSquare.from_SAN(self.san).valid():
            raise RuntimeError(InvalidFromSquare.from_index_with_SANs(self.index, self.sans).created())

        return self

    def valid_to_square(self) -> ValidMicroSAN:
        if not ToSquare.from_SAN(self.san).valid():
            raise RuntimeError(InvalidToSquare.from_index_with_SANs(self.index, self.sans).created())

        return self

    def valid_promotion(self) -> ValidMicroSAN:
        if len(self.san) == 5 and self.san[4] not in "QqRrBbNn":
            raise RuntimeError(InvalidPromotion.from_index_with_SANs(self.index, self.sans).created())

        return self
