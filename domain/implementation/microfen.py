# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from typing import NamedTuple

from .basictype import FEN


class MicroFEN(NamedTuple):
    index: int
    fens: list[str]
    fen: FEN

    @classmethod
    def from_index_with_FENs(cls, index: int, fens: list[str]) -> MicroFEN:
        return MicroFEN(index, fens, FEN(fens[index]))
