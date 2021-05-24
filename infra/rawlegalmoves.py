# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

import chess


class RawUci(str):
    @classmethod
    def from_move(cls, move: chess.Move) -> RawUci:
        return RawUci(move.uci())

    @classmethod
    def black_castling(cls) -> RawUci:
        return RawUci("e8g8")


class RawMove(str):
    @classmethod
    def from_uci(cls, uci: RawUci) -> RawMove:
        return RawMove(uci)

    @classmethod
    def castling(cls) -> RawMove:
        return RawMove("O-O")

    @classmethod
    def from_move(cls, move: chess.Move) -> RawMove:
        rawuci: RawUci = RawUci.from_move(move)

        return RawMove.castling() if rawuci == RawUci.black_castling() else RawMove.from_uci(rawuci)


class RawLegalMoves(list[str]):
    @classmethod
    def from_original_legal_moves(cls, legal_moves: chess.LegalMoveGenerator) -> RawLegalMoves:
        return RawLegalMoves([RawMove.from_move(move) for move in legal_moves])

    @classmethod
    def from_FEN(cls, fen: str) -> RawLegalMoves:
        return RawLegalMoves.from_original_legal_moves(chess.Board(fen).legal_moves)

    @classmethod
    def castling(cls) -> RawLegalMoves:
        return RawLegalMoves([RawMove.castling()])

    def castlable(self) -> bool:
        return RawMove.castling() in self

    def corrected(self, mirrored: str) -> RawLegalMoves:
        return RawLegalMoves(self + (RawLegalMoves.castling() if RawLegalMoves.from_FEN(mirrored).castlable() else []))
