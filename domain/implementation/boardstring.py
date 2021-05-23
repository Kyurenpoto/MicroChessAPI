# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from functools import reduce
from typing import NamedTuple

from domain.error.boardstringerror import InvalidPieceNumber, NotEmptyOutside

from .mappable import Mappable
from .microfen import MicroFEN
from .symbol import ExpandedSymbol


class BoardString(NamedTuple):
    microfen: MicroFEN
    board: str

    @classmethod
    def from_MicroFEN(cls, microfen: MicroFEN) -> BoardString:
        return BoardString(microfen, "".join(map(lambda x: ExpandedSymbol.from_symbol(x), microfen.fen.split(" ")[0])))


class EmptyOutsideMicroBoardString(BoardString):
    @classmethod
    def from_boardstring(cls, board: BoardString) -> EmptyOutsideMicroBoardString:
        if (
            reduce(lambda x, y: x | y, [set(board.board[i : i + 4]) for i in range(0, 40, 8)]) | set(board.board[40:])
        ) != set("."):
            raise RuntimeError(NotEmptyOutside.from_index_with_FENs(board.microfen.index, board.microfen.fens))

        return EmptyOutsideMicroBoardString(board.microfen, board.board)


class PieceRange(NamedTuple):
    min_val: int
    max_val: int

    @classmethod
    def from_symbol(cls, symbol: str) -> PieceRange:
        if symbol in "Kk":
            return PieceRange(1, 1)
        if symbol in "QqPp":
            return PieceRange(0, 1)

        return PieceRange(0, 2)

    def contained(self, x: int) -> bool:
        return self.min_val <= x <= self.max_val


class PieceCountValidMicroBoardString(BoardString):
    @classmethod
    def from_boardstring(cls, board: BoardString) -> PieceCountValidMicroBoardString:
        pieces: str = board.board.replace(".", "")
        for i in "KkQqPpRrBbNn":
            if not PieceRange.from_symbol(i).contained(pieces.count(i)):
                raise RuntimeError(InvalidPieceNumber.from_index_with_FENs(board.microfen.index, board.microfen.fens))

        for i in "QqRrBbNn":
            if pieces.count(i) + pieces.count("P" if i.isupper() else "p") > PieceRange.from_symbol(i).max_val:
                raise RuntimeError(InvalidPieceNumber.from_index_with_FENs(board.microfen.index, board.microfen.fens))

        return PieceCountValidMicroBoardString(board.microfen, board.board)


class ValidMicroBoardString(BoardString):
    @classmethod
    def from_boardstring(cls, board: BoardString) -> ValidMicroBoardString:
        valid: BoardString = (
            Mappable(EmptyOutsideMicroBoardString.from_boardstring(board))
            .mapped(lambda x: PieceCountValidMicroBoardString.from_boardstring(x))
            .value()
        )

        return ValidMicroBoardString(valid.microfen, valid.board)
