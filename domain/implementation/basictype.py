# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations


class FEN(str):
    @classmethod
    def starting(cls) -> FEN:
        return FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")

    @classmethod
    def first_move(cls) -> FEN:
        return FEN("4knbr/4p3/7P/8/4RBNK/8/8/8 b Kk - 0 1")

    @classmethod
    def checkmate(cls) -> FEN:
        return FEN("4k3/6B1/4R1K1/4p3/8/8/8/8 b Kk - 0 1")

    @classmethod
    def stalemate(cls) -> FEN:
        return FEN("4k3/4pR1K/4RPB1/8/8/8/8/8 b Kk - 0 1")

    @classmethod
    def black_castlable(cls) -> FEN:
        return FEN("4k2r/4p3/8/7P/4RBNK/8/8/8 b Kk - 0 1")

    @classmethod
    def white_castlable(cls) -> FEN:
        return FEN("4knbr/4p3/8/7P/4R2K/8/8/8 w Kk - 0 1")

    @classmethod
    def black_castled(cls) -> FEN:
        return FEN("5rk1/4p3/8/7P/4RBNK/8/8/8 w K - 1 2")

    @classmethod
    def white_castled(cls) -> FEN:
        return FEN("4knbr/4p3/8/7P/5KR1/8/8/8 b k - 1 1")

    @classmethod
    def only_king(cls) -> FEN:
        return FEN("4k3/8/8/8/7K/8/8/8 w - - 0 1")

    @classmethod
    def swap_king_bishop(cls) -> FEN:
        return FEN("4knbr/4p3/8/7P/4RK1B/8/8/8 w Kk - 0 1")


class SAN(str):
    @classmethod
    def castling(cls) -> SAN:
        return SAN("O-O")

    @classmethod
    def first_move(cls) -> SAN:
        return SAN("h5h6")

    @classmethod
    def second_move(cls) -> SAN:
        return SAN("e7e6")

    @classmethod
    def king_side_move(cls) -> SAN:
        return SAN("h4g4")

    @classmethod
    def black_double_move(cls) -> SAN:
        return SAN("e7e5")
