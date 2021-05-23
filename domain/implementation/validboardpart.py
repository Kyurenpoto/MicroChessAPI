# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from domain.error.boardstringerror import InvalidRowNumber, InvalidSquareNumber, InvalidSymbol

from .mappable import Mappable
from .splitablefen import BoardPart
from .symbol import ExpandedSymbol


class SqueezedSymbol(str):
    @classmethod
    def valid_set(cls) -> set[str]:
        return set("12345678/PpKkQqRrNnBb")


class SymbolValidBoardPart(BoardPart):
    @classmethod
    def from_raw(cls, raw: BoardPart) -> SymbolValidBoardPart:
        if not SqueezedSymbol.valid_set().issuperset(set(raw.board)):
            raise RuntimeError(InvalidSymbol.from_index_with_FENs(raw.fen.index, raw.fen.fens))

        return SymbolValidBoardPart(raw.fen, raw.board)


class SizeValidBoardPart(BoardPart):
    @classmethod
    def from_raw(cls, raw: BoardPart) -> SizeValidBoardPart:
        splited: list[str] = raw.board.split("/")
        if len(splited) != 8:
            raise RuntimeError(InvalidRowNumber.from_index_with_FENs(raw.fen.index, raw.fen.fens))
        for row in splited:
            if len("".join(map(lambda x: ExpandedSymbol.from_symbol(x), row))) != 8:
                raise RuntimeError(InvalidSquareNumber.from_index_with_FENs(raw.fen.index, raw.fen.fens))

        return SizeValidBoardPart(raw.fen, raw.board)


class ValidBoardPart(BoardPart):
    @classmethod
    def from_raw(cls, raw: BoardPart) -> ValidBoardPart:
        valid = Mappable(SymbolValidBoardPart.from_raw(raw)).mapped(lambda x: SizeValidBoardPart.from_raw(x)).value()

        return ValidBoardPart(valid.fen, valid.board)
