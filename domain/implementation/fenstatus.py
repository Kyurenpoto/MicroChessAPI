# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, Optional

from domain.implementation.microfen import MicroFEN
from infra.rawcheckedfen import RawCheckedFEN

from .basictype import FEN
from .boardstring import BoardString
from .microboardstatus import MicroBoardStatus

PAWN: Final[dict[str, str]] = {"w": "P", "b": "p"}
QUEEN: Final[dict[str, str]] = {"w": "Q", "b": "q"}
ROOK: Final[dict[str, str]] = {"w": "R", "b": "r"}
KNIGHT: Final[dict[str, str]] = {"w": "N", "b": "n"}
BISHOP: Final[dict[str, str]] = {"w": "B", "b": "b"}
OPPONENT: Final[dict[str, str]] = {"w": "b", "b": "w"}


def with_pawn_queen_rook(board: str, color: str) -> bool:
    return board.count(PAWN[color]) + board.count(QUEEN[color]) + board.count(ROOK[color]) > 0


def knight_with_opponent_pawn_rook_knight_bishop(board: str, color: str) -> bool:
    return board.count(KNIGHT[color]) == 1 and (
        board.count(BISHOP[color]) > 0
        or (
            board.count(PAWN[OPPONENT[color]])
            + board.count(ROOK[OPPONENT[color]])
            + board.count(KNIGHT[OPPONENT[color]])
            + board.count(BISHOP[OPPONENT[color]])
            > 0
        )
    )


def square_color(loc: int) -> int:
    return ((loc // 8) + (loc % 8)) % 2


def same_color_bishop_with_opponent_pawn_knight(board: str, color: str) -> bool:
    loc1: int = board.find(BISHOP[color])
    if loc1 == -1:
        return False

    loc2: int = board.find(BISHOP[color], loc1 + 1)
    return (loc2 != -1 and square_color(loc1) != square_color(loc2)) or board.count(
        PAWN[OPPONENT[color]]
    ) + board.count(KNIGHT[OPPONENT[color]]) > 0


class SufficientMeterialFEN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[FEN]:
        board: str = BoardString(MicroFEN(0, [self.__fen])).value()
        color: str = self.__fen.split(" ")[1]
        if with_pawn_queen_rook(board, color):
            return self.__fen
        if knight_with_opponent_pawn_rook_knight_bishop(board, color):
            return self.__fen
        if same_color_bishop_with_opponent_pawn_knight(board, color):
            return self.__fen

        return None


class InnerFiftyMovesFEN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[FEN]:
        return self.__fen if int(self.__fen.split(" ")[-2]) < 50 else None


class FENStatus:
    __slots__ = ["__fen", "__cnt_legal_moves"]

    __fen: FEN
    __cnt_legal_moves: int

    def __init__(self, fen: FEN, cnt_legal_moves: int):
        self.__fen = fen
        self.__cnt_legal_moves = cnt_legal_moves

    def value(self) -> MicroBoardStatus:
        if SufficientMeterialFEN(self.__fen).value() is None:
            return MicroBoardStatus.INSUFFICIENT_MATERIAL
        if InnerFiftyMovesFEN(self.__fen).value() is None:
            return MicroBoardStatus.FIFTY_MOVES
        if self.__cnt_legal_moves == 0:
            return (
                MicroBoardStatus.STALEMATE if RawCheckedFEN(self.__fen).value() is None else MicroBoardStatus.CHECKMATE
            )

        return MicroBoardStatus.NONE
