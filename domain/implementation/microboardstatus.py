# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from enum import Enum, auto
from functools import reduce
from typing import NamedTuple

from domain.implementation.boardstring import BoardString
from domain.implementation.microfen import MicroFEN
from infra.rawcheckedfen import RawCheckedFEN

from .basictype import FEN
from .splitablefen import ColorPart, HalfmovePart


def square_color(loc: int) -> int:
    return ((loc // 8) + (loc % 8)) % 2


class CountableBoardPart(str):
    @classmethod
    def from_FEN(cls, fen: FEN) -> CountableBoardPart:
        return CountableBoardPart(BoardString.from_MicroFEN(MicroFEN.from_index_with_FENS(0, [fen])).board)

    def count_symbols(self, symbols: str) -> int:
        return reduce(lambda x, y: x + y, [self.count(x) for x in symbols])

    def different_color_location(self, symbol: str) -> bool:
        loc1: int = self.find(symbol)
        if loc1 == -1:
            return False

        loc2: int = self.find(symbol, loc1 + 1)
        return loc2 != -1 and square_color(loc1) != square_color(loc2)


class SymbolizableColorPart(ColorPart):
    @classmethod
    def from_FEN(cls, fen: FEN) -> SymbolizableColorPart:
        return SymbolizableColorPart(ColorPart.from_FEN(fen))

    def opposite(self) -> SymbolizableColorPart:
        return SymbolizableColorPart(self.mirror())

    def pawn_queen_rook(self) -> str:
        return {"w": "PQR", "b": "pqr"}[self]

    def pawn_rook_knight_bishop(self) -> str:
        return {"w": "PRNB", "b": "prnb"}[self]

    def pawn(self) -> str:
        return {"w": "P", "b": "p"}[self]

    def knight(self) -> str:
        return {"w": "N", "b": "n"}[self]

    def bishop(self) -> str:
        return {"w": "B", "b": "b"}[self]


class BoardColorPart(NamedTuple):
    board: CountableBoardPart
    color: SymbolizableColorPart

    @classmethod
    def from_FEN(cls, fen: FEN) -> BoardColorPart:
        return BoardColorPart(CountableBoardPart.from_FEN(fen), SymbolizableColorPart.from_FEN(fen))

    def insufficient(self) -> bool:
        return not (
            self.with_pawn_queen_rook()
            or self.knight_with_opposite_pawn_rook_knight_bishop()
            or self.same_color_bishop_with_opponent_pawn_knight()
        )

    def with_pawn_queen_rook(self) -> bool:
        return self.board.count_symbols(self.color.pawn_queen_rook()) > 0

    def knight_with_opposite_pawn_rook_knight_bishop(self) -> bool:
        return self.board.count(self.color.knight()) == 1 and (
            self.board.count(self.color.bishop()) > 0
            or self.board.count_symbols(self.color.opposite().pawn_rook_knight_bishop()) > 0
        )

    def same_color_bishop_with_opponent_pawn_knight(self) -> bool:
        if self.board.count(self.color.bishop()) == 0:
            return False

        return (
            self.board.different_color_location(self.color.bishop())
            or self.board.count(self.color.opposite().pawn()) + self.board.count(self.color.opposite().knight()) > 0
        )


class ConditionalHalfmovePart(HalfmovePart):
    @classmethod
    def from_FEN(cls, fen: FEN) -> ConditionalHalfmovePart:
        return ConditionalHalfmovePart(HalfmovePart.from_FEN(fen))

    def over_fifty_moves(self) -> bool:
        return self >= 50


class StatusClue(NamedTuple):
    fen: FEN
    cnt_legal_moves: int


class MicroBoardStatus(Enum):
    NONE = auto()
    CHECKMATE = auto()
    STALEMATE = auto()
    INSUFFICIENT_MATERIAL = auto()
    FIFTY_MOVES = auto()

    @classmethod
    def from_status_check_clue(cls, clue: StatusClue) -> MicroBoardStatus:
        if clue.cnt_legal_moves == 0:
            return (
                MicroBoardStatus.STALEMATE if RawCheckedFEN(clue.fen).checked() is None else MicroBoardStatus.CHECKMATE
            )

        return MicroBoardStatus.NONE

    @classmethod
    def from_status_clue(cls, clue: StatusClue) -> MicroBoardStatus:
        if BoardColorPart.from_FEN(clue.fen).insufficient():
            return MicroBoardStatus.INSUFFICIENT_MATERIAL
        if ConditionalHalfmovePart.from_FEN(clue.fen).over_fifty_moves():
            return MicroBoardStatus.FIFTY_MOVES
        return MicroBoardStatus.from_status_check_clue(clue)

    @classmethod
    def from_fen_with_legal_moves(cls, fen: FEN, cnt_legal_moves: int) -> MicroBoardStatus:
        return MicroBoardStatus.from_status_clue(StatusClue(fen, cnt_legal_moves))
