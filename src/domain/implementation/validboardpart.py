# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from src.domain.error.boardparterror import InvalidRowNumber, InvalidSquareNumber, InvalidSymbol
from src.domain.implementation.boardstring import BoardString, ValidMicroBoardString
from src.domain.implementation.splitablefen import BoardPart
from src.domain.implementation.symbol import ExpandedSymbol


class ValidBoardPart(BoardPart):
    @classmethod
    def from_raw(cls, raw: BoardPart) -> ValidBoardPart:
        return ValidBoardPart._make(raw).valid_symbol().valid_size().valid_board_string()

    def valid_symbol(self) -> ValidBoardPart:
        if not set(self.board).issubset(set("12345678/PpKkQqRrNnBb")):
            raise RuntimeError(InvalidSymbol.from_index_with_FENs(self.fen.index, self.fen.fens))

        return self

    def valid_size(self) -> ValidBoardPart:
        splited: list[str] = self.board.split("/")
        if len(splited) != 8:
            raise RuntimeError(InvalidRowNumber.from_index_with_FENs(self.fen.index, self.fen.fens))
        for row in splited:
            if len("".join(map(lambda x: ExpandedSymbol.from_symbol(x), row))) != 8:
                raise RuntimeError(InvalidSquareNumber.from_index_with_FENs(self.fen.index, self.fen.fens))

        return self

    def valid_board_string(self) -> ValidBoardPart:
        return ValidBoardPart._make(
            BoardPart.from_MicroFEN(
                ValidMicroBoardString.from_boardstring(BoardString.from_MicroFEN(self.fen)).microfen
            )
        )
