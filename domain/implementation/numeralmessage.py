# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations


class NumeralMessage(str):
    @classmethod
    def from_numeral(cls, numeral: str) -> NumeralMessage:
        return NumeralMessage(f"At the {numeral} element: ")

    @classmethod
    def from_index(cls, index: int) -> NumeralMessage:
        if index == 1:
            return NumeralMessage.from_numeral("1st")
        if index == 2:
            return NumeralMessage.from_numeral("2nd")
        if index == 3:
            return NumeralMessage.from_numeral("3rd")

        return NumeralMessage.from_numeral(f"{index}th")
