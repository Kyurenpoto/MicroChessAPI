# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, NamedTuple

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
VALID_SQUARES: Final[set[str]] = set([i + j for j in "45678" for i in "efgh"])


class LengthValidSAN(NamedTuple):
    san: MicroSAN

    def value(self) -> MicroSAN:
        if not (4 <= len(self.san.san()) <= 5):
            raise RuntimeError(InvalidLength.from_index_with_SANs(self.san.index(), self.san.sans()))

        return self.san


class FromSquareValidSAN(NamedTuple):
    san: MicroSAN

    def value(self) -> MicroSAN:
        if self.san.san()[:2] not in VALID_SQUARES:
            raise RuntimeError(InvalidFromSquare.from_index_with_SANs(self.san.index(), self.san.sans()))

        return self.san


class ToSquareValidSAN(NamedTuple):
    san: MicroSAN

    def value(self) -> MicroSAN:
        if self.san.san()[2:4] not in VALID_SQUARES:
            raise RuntimeError(InvalidToSquare.from_index_with_SANs(self.san.index(), self.san.sans()))

        return self.san


class PromotionValidSAN(NamedTuple):
    san: MicroSAN

    def value(self) -> MicroSAN:
        if len(self.san.san()) == 5 and self.san.san()[4] not in PROMOTIONABLE_PIECES:
            raise RuntimeError(InvalidPromotion.from_index_with_SANs(self.san.index(), self.san.sans()))

        return self.san


class ValidMicroSAN(NamedTuple):
    san: MicroSAN

    def value(self) -> MicroSAN:
        return (
            self.san
            if self.san.san() == MICRO_CASTLING_SAN
            else (
                Mappable(LengthValidSAN(self.san).value())
                .mapped(lambda x: FromSquareValidSAN(x).value())
                .mapped(lambda x: ToSquareValidSAN(x).value())
                .mapped(lambda x: PromotionValidSAN(x).value())
                .value()
            )
        )
