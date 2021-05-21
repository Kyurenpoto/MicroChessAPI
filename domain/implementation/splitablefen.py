# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from domain.implementation.microfen import MicroFEN

from .boardstring import BoardString


class BoardPart(str):
    @classmethod
    def from_FEN(cls, fen: str) -> BoardPart:
        return BoardPart(BoardString(MicroFEN(0, [fen])).value())


class ColorPart(str):
    @classmethod
    def from_FEN(cls, fen: str) -> ColorPart:
        return ColorPart(fen.split(" ")[1])
