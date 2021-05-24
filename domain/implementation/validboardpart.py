# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from domain.error.boardparterror import InvalidRowNumber, InvalidSquareNumber, InvalidSymbol

from .boardstring import BoardString, ValidMicroBoardString
from .splitablefen import BoardPart
from .symbol import ExpandedSymbol


class ValidBoardPart(BoardPart):
    @classmethod
    def from_raw(cls, raw: BoardPart) -> ValidBoardPart:
        return ValidBoardPart(raw.fen, raw.board).valid_symbol().valid_size().valid_board_string()

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
        valid: BoardPart = BoardPart.from_MicroFEN(
            ValidMicroBoardString.from_boardstring(BoardString.from_MicroFEN(self.fen)).microfen
        )

        return ValidBoardPart(valid.fen, valid.board)
