# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from .basictype import SAN


class Square(str):
    def file(self) -> str:
        return self[0]

    def rank(self) -> str:
        return self[1]

    @classmethod
    def valid_set(cls) -> set[Square]:
        return set([Square(i + j) for j in "45678" for i in "efgh"])


class FromSquare(Square):
    @classmethod
    def from_SAN(cls, san: SAN) -> FromSquare:
        return FromSquare(san[:2])


class ToSquare(Square):
    @classmethod
    def from_SAN(cls, san: SAN) -> FromSquare:
        return FromSquare(san[2:4])
