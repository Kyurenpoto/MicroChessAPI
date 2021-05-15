# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, Set

from domain.error.microfenerror import (
    InvalidCastlingPart,
    InvalidEnpassantPart,
    InvalidFullmovePart,
    InvalidHalfmovePart,
    InvalidStructure,
    InvalidTurnPart,
)

from .basictype import FEN
from .boardstring import BoardString, ValidMicroBoardString
from .mappable import Mappable
from .microfen import MicroFEN

MICRO_STARTING_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")
MICRO_FIRST_MOVE_FEN: Final[FEN] = FEN("4knbr/4p3/7P/8/4RBNK/8/8/8 b Kk - 0 1")
MICRO_CHECKMATE_FEN: Final[FEN] = FEN("4k3/6B1/4R1K1/4p3/8/8/8/8 b Kk - 0 1")
MICRO_STALEMATE_FEN: Final[FEN] = FEN("4k3/4pR1K/4RPB1/8/8/8/8/8 b Kk - 0 1")
MICRO_BLACK_CASTLABLE_FEN: Final[FEN] = FEN("4k2r/4p3/8/7P/4RBNK/8/8/8 b Kk - 0 1")
MICRO_WHITE_CASTLABLE_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/4R2K/8/8/8 w Kk - 0 1")
MICRO_BLACK_CASTLED_FEN: Final[FEN] = FEN("5rk1/4p3/8/7P/4RBNK/8/8/8 w K - 1 2")
MICRO_WHITE_CASTLED_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/5KR1/8/8/8 b k - 1 1")
MICRO_ONLY_KING_FEN: Final[FEN] = FEN("4k3/8/8/8/7K/8/8/8 w - - 0 1")
MICRO_SWAP_KING_BISHOP_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/4RK1B/8/8/8 w Kk - 0 1")


class ValidStructedMicroFEN:
    __slots__ = ["__fen"]

    __fen: MicroFEN

    def __init__(self, fen: MicroFEN):
        self.__fen = fen

    def value(self) -> MicroFEN:
        if len(self.__fen.fen().split(" ")) != 6:
            raise RuntimeError(InvalidStructure(self.__fen.index(), self.__fen.fens()).value())

        return self.__fen


class ValidBoardPartMicroFEN:
    __slots__ = ["__fen"]

    __fen: MicroFEN

    def __init__(self, fen: MicroFEN):
        self.__fen = fen

    def value(self) -> MicroFEN:
        return ValidMicroBoardString(BoardString(self.__fen)).value().fen()


VALID_TURN_PART: Final[Set[str]] = set(["w", "b"])


class ValidTurnPartMicroFEN:
    __slots__ = ["__fen"]

    __fen: MicroFEN

    def __init__(self, fen: MicroFEN):
        self.__fen = fen

    def value(self) -> MicroFEN:
        if self.__fen.fen().split(" ")[1] not in VALID_TURN_PART:
            raise RuntimeError(InvalidTurnPart(self.__fen.index(), self.__fen.fens()).value())

        return self.__fen


VALID_CASTLING_PART: Final[Set[str]] = set(["Kk", "K", "k", "-"])


class ValidCastlingPartMicroFEN:
    __slots__ = ["__fen"]

    __fen: MicroFEN

    def __init__(self, fen: MicroFEN):
        self.__fen = fen

    def value(self) -> MicroFEN:
        if self.__fen.fen().split(" ")[2] not in VALID_CASTLING_PART:
            raise RuntimeError(InvalidCastlingPart(self.__fen.index(), self.__fen.fens()).value())

        return self.__fen


class ValidEnpassantPartMicroFEN:
    __slots__ = ["__fen"]

    __fen: MicroFEN

    def __init__(self, fen: MicroFEN):
        self.__fen = fen

    def value(self) -> MicroFEN:
        if self.__fen.fen().split(" ")[3] != "-":
            raise RuntimeError(InvalidEnpassantPart(self.__fen.index(), self.__fen.fens()).value())

        return self.__fen


class ValidHalfmovePartMicroFEN:
    __slots__ = ["__fen"]

    __fen: MicroFEN

    def __init__(self, fen: MicroFEN):
        self.__fen = fen

    def value(self) -> MicroFEN:
        halfmove: str = self.__fen.fen().split(" ")[4]
        if not (halfmove.isdigit() and 0 <= int(halfmove) <= 50):
            raise RuntimeError(InvalidHalfmovePart(self.__fen.index(), self.__fen.fens()).value())

        return self.__fen


class ValidFullmovePartMicroFEN:
    __slots__ = ["__fen"]

    __fen: MicroFEN

    def __init__(self, fen: MicroFEN):
        self.__fen = fen

    def value(self) -> MicroFEN:
        fullmove: str = self.__fen.fen().split(" ")[5]
        if not (fullmove.isdigit() and 1 <= int(fullmove) <= 80):
            raise RuntimeError(InvalidFullmovePart(self.__fen.index(), self.__fen.fens()).value())

        return self.__fen


class ValidMicroFEN:
    __slots__ = ["__fen"]

    __fen: MicroFEN

    def __init__(self, fen: MicroFEN):
        self.__fen = fen

    def value(self) -> MicroFEN:
        return (
            Mappable(ValidStructedMicroFEN(self.__fen).value())
            .mapped(lambda x: ValidBoardPartMicroFEN(x).value())
            .mapped(lambda x: ValidTurnPartMicroFEN(x).value())
            .mapped(lambda x: ValidCastlingPartMicroFEN(x).value())
            .mapped(lambda x: ValidEnpassantPartMicroFEN(x).value())
            .mapped(lambda x: ValidHalfmovePartMicroFEN(x).value())
            .mapped(lambda x: ValidFullmovePartMicroFEN(x).value())
            .value()
        )
