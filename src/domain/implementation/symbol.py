# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations


class ExpandedSymbol(str):
    @classmethod
    def from_symbol(cls, symbol: str) -> ExpandedSymbol:
        if symbol.isdecimal():
            return ExpandedSymbol("." * int(symbol))
        if symbol == "/":
            return ExpandedSymbol("")

        return ExpandedSymbol(symbol)
