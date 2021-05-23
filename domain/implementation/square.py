# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from .basictype import SAN


class Square(str):
    def file(self) -> str:
        return self[0]

    def rank(self) -> str:
        return self[1]

    def valid(self) -> bool:
        return (self.file() in "efgh") and (self.rank() in "45678")


class FromSquare(Square):
    @classmethod
    def from_SAN(cls, san: SAN) -> FromSquare:
        return FromSquare(san[:2])


class ToSquare(Square):
    @classmethod
    def from_SAN(cls, san: SAN) -> FromSquare:
        return FromSquare(san[2:4])
