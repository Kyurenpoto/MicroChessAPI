# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from typing import NamedTuple

from domain.error.movetargeterror import (
    CannotCastle,
    EmptyFromSquare,
    FullToSquare,
    InvalidPieceMove,
    OppositeFromSquare,
)
from domain.implementation.validmicrofen import ValidMicroFEN

from .basictype import FEN, SAN
from .boardstring import BoardString
from .legalsan import LegalSANs
from .microfen import MicroFEN
from .microsan import MicroSAN, ValidMicroSAN
from .movablefen import MovableFEN
from .splitablefen import ColorPart
from .square import FromSquare, Square, ToSquare


class MoveTarget(NamedTuple):
    index: int
    fens: list[str]
    sans: list[str]
    fen: FEN
    san: SAN

    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> MoveTarget:
        return MoveTarget(
            index,
            fens,
            sans,
            ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(index, fens)).fen,
            ValidMicroSAN.from_MicroSAN(MicroSAN.from_index_with_SANs(index, sans)).san,
        )


class Piece(str):
    @classmethod
    def from_board_with_square(cls, board: BoardString, square: Square):
        file_val: int = ord(square.file()) - ord("a")
        rank_val: int = ord(square.rank()) - ord("1")

        return Piece(board.board[file_val + ((7 - rank_val) * 8)])

    def color(self) -> str:
        return "w" if self.isupper() else "b"


class ValidMoveTarget(MoveTarget):
    @classmethod
    def from_move_target(cls, target: MoveTarget) -> ValidMoveTarget:
        return (
            ValidMoveTarget._make(target).castling_in_legal_moves()
            if target.san == SAN.castling()
            else (ValidMoveTarget._make(target).valid_from_square_piece().valid_to_square_piece().san_in_legal_moves())
        )

    def castling_in_legal_moves(self) -> ValidMoveTarget:
        if SAN.castling() not in LegalSANs.from_FEN(
            self.fen if ColorPart.from_FEN(self.fen) == "b" else MovableFEN(self.fen).mirrored()
        ):
            raise RuntimeError(CannotCastle.from_index_with_FENs_SANs(self.index, self.fens, self.sans))

        return self

    def valid_from_square_piece(self) -> ValidMoveTarget:
        piece: Piece = Piece.from_board_with_square(
            BoardString.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [self.fen])), FromSquare.from_SAN(self.san)
        )
        if piece == ".":
            raise RuntimeError(EmptyFromSquare.from_index_with_FENs_SANs(self.index, self.fens, self.sans))
        if piece.color() != ColorPart.from_FEN(self.fen):
            raise RuntimeError(OppositeFromSquare.from_index_with_FENs_SANs(self.index, self.fens, self.sans))

        return self

    def valid_to_square_piece(self) -> ValidMoveTarget:
        piece: Piece = Piece.from_board_with_square(
            BoardString.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [self.fen])), ToSquare.from_SAN(self.san)
        )
        if piece != "." and piece.color() == ColorPart.from_FEN(self.fen):
            raise RuntimeError(FullToSquare.from_index_with_FENs_SANs(self.index, self.fens, self.sans))

        return self

    def san_in_legal_moves(self) -> ValidMoveTarget:
        if self.san not in LegalSANs.from_FEN(self.fen):
            raise RuntimeError(InvalidPieceMove.from_index_with_FENs_SANs(self.index, self.fens, self.sans))

        return self
