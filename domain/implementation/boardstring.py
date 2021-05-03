# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, Optional, List, Dict, NewType, cast

from infra.rawboardstring import RawBoardString
from .extendtype import Nullable

FEN = NewType('FEN', str)

class BoardString:
    __slots__ = ["__board"]

    __board: List[str]

    def __init__(self, board: RawBoardString):
        self.__board = ["".join(line.split(" ")) for line in str(board).split("\n")]

    def value(self) -> List[str]:
        return self.__board

    def empty(self) -> bool:
        return "".join(self.__board) == ("." * 64)

class MicroPartBoardString:
    __slots__ = ["__board"]

    __board: List[str]

    def __init__(self, board: BoardString):
        self.__board = board.value()

    def value(self) -> str:
        return "".join([i[4:8] for i in self.__board[0:5]])

class MicroPartBoardPiece:
    __slots__ = ["__board"]

    __board: MicroPartBoardString

    def __init__(self, board: BoardString):
        self.__board = MicroPartBoardString(board)

    def value(self) -> str:
        return self.__board.value().replace(".", "")

class PieceRangeValidMicroBoardString:
    __slots__ = ["__board"]
    
    __board: Optional[BoardString]

    def __init__(self, board: Optional[BoardString]):
        self.__board = board

    def value(self) -> Optional[BoardString]:
        if self.__board is None:
            return None

        board = cast(BoardString, self.__board).value()
        for i in range(0, 5):
            if board[i][0:4] != "....":
                return None
        for i in range(5, 8):
            if board[i] != "........":
                return None

        return self.__board

CHESS_PIECES: Final[str] = "KkQqPpRrBbNn"

class PieceRange:
    __slots__ = ["min_val", "max_val"]

    min_val: int
    max_val: int

    def __init__(self, a: int, b: int):
        self.min_val = a
        self.max_val = b

    def contained(self, x: int) -> bool:
        return self.min_val <= x <= self.max_val

MICROCHESS_PIECE_RANGES: Final[Dict[str, PieceRange]] = dict(zip(
    CHESS_PIECES,
    ([PieceRange(1, 1)] * 2) + ([PieceRange(0, 1)] * 4) + ([PieceRange(0, 2)] * 6)))

class PieceCountValidMicroBoardString:
    __slots__ = ["__board"]
    
    __board: Optional[BoardString]

    def __init__(self, board: Optional[BoardString]):
        self.__board = board

    def value(self) -> Optional[BoardString]:
        if self.__board is None:
            return None

        cnt: Dict[str, int] = {i:0 for i in CHESS_PIECES}
        for i in MicroPartBoardPiece(cast(BoardString, self.__board)).value():
            cnt[i] += 1

        for i in CHESS_PIECES:
            if MICROCHESS_PIECE_RANGES[i].contained(cnt[i]) is False:
                return None
        
        return self.__board

class ValidMicroBoardString:
    __slots__ = ["__board"]
    
    __board: Optional[BoardString]

    def __init__(self, board: Optional[BoardString]):
        self.__board = board

    def value(self) -> Optional[BoardString]:
        return Nullable(self.__board).op(
            lambda x: PieceRangeValidMicroBoardString(x).value()).op(
            lambda x: PieceCountValidMicroBoardString(x).value()).value()
