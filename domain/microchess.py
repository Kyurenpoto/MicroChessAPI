# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations
from enum import Enum
from typing import Optional, Final, List, Tuple

from infra.rawmovedfen import RawMovedFen
from infra.rawlegalmoves import RawLegalMoves
from infra.rawcheckedboard import RawCheckedBoard
from .implementation.boardstring import FEN
from .implementation.microfen import ValidMicroFen, MirroredMicroFen
from .implementation.microsan import ValidMicroSAN, SAN, MICRO_CASTLING_SAN

MICRO_STARTING_FEN: Final[FEN] = FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")
class MicroMove:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN = MICRO_CASTLING_SAN):
        self.__san = san

    def san(self) -> SAN:
        return self.__san

class CreatedMicroMove:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: str):
        self.__san = SAN(san)

    def value(self) -> MicroMove:
        san: Optional[SAN] = ValidMicroSAN(self.__san).value()
        if san is None:
            raise RuntimeError("Invalid SAN")

        return MicroMove(san)

class MicroBoard:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN = MICRO_STARTING_FEN):
        self.__fen = fen

    def fen(self) -> FEN:
        return self.__fen

class CreatedMicroBoard:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: str):
        self.__fen = FEN(fen)

    def value(self) -> MicroBoard:
        fen: Optional[FEN] = ValidMicroFen(self.__fen).value()
        if fen is None:
            raise RuntimeError("Invalid FEN")
        
        return MicroBoard(fen)

class MovedMicroBoard:
    __slots__ = ["__fen", "__san"]

    __fen: FEN
    __san: SAN

    def __init__(self, fen: FEN, san: SAN):
        self.__fen = fen
        self.__san = san

    def value(self) -> MicroBoard:
        board: MicroBoard = CreatedMicroBoard(self.__fen).value()
        move: MicroMove = CreatedMicroMove(self.__san).value()

        if move.san() == MICRO_CASTLING_SAN:
            mirrored: FEN = MirroredMicroFen(board.fen()).value()
            moved: FEN = FEN(str(RawMovedFen(mirrored, move.san())))

            return MicroBoard(MirroredMicroFen(moved).value())
        else:
            return MicroBoard(FEN(str(RawMovedFen(board.fen(), move.san()))))

class LegalFENs:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> List[SAN]:
        legal_moves: List[SAN] = []
        for san in RawLegalMoves(self.__fen).value():
            valid = ValidMicroSAN(SAN(san)).value()
            if (valid is not None and
                valid != "e7e5"):
                legal_moves += [valid]

        return sorted(legal_moves)

class MicroBoardStatus(Enum):
    NONE = 0
    CHECKMATE = 1
    STALEMATE = 2

class FENStatus:
    __slots__ = ["__fen", "__cnt_legal_moves"]

    __fen: FEN
    __cnt_legal_moves: int

    def __init__(self, fen: FEN, cnt_legal_moves: int):
        self.__fen = fen
        self.__cnt_legal_moves = cnt_legal_moves

    def value(self) -> MicroBoardStatus:
        if self.__cnt_legal_moves != 0:
            return MicroBoardStatus.NONE

        return (MicroBoardStatus.CHECKMATE
            if RawCheckedBoard(self.__fen).value()
            else MicroBoardStatus.STALEMATE)

class ModelActResult:
    __slots__ = ["__fens", "__sans"]

    __fens: List[FEN]
    __sans: List[SAN]

    def __init__(self, fens: List[str], sans: List[str]):
        self.__fens = [FEN(fen) for fen in fens]
        self.__sans = [SAN(san) for san in sans]

    def value(self) -> Tuple[List[str], List[List[str]], List[MicroBoardStatus]]:
        moved: List[str] = [
            str(MovedMicroBoard(fen, san).value().fen())
            for fen, san in zip(self.__fens, self.__sans)]
        legal_moves: List[List[str]] = [[str(san) for san in LegalFENs(FEN(fen)).value()]
            for fen in moved]
        statuses: List[MicroBoardStatus] = [FENStatus(FEN(fen), len(moves)).value()
            for fen, moves in zip(moved, legal_moves)]
        
        return moved, legal_moves, statuses
