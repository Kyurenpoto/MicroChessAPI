# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, List

from domain.dto.modeldto import ModelErrorResponse
from domain.implementation.indexmessage import IndexMessage

MSG_CANNOT_CASTLE: Final[
    str
] = "Castling is only possible when FEN's castling availability is active and between king and rook is empty"
MSG_EMPTY_FROM_SQUARE: Final[str] = "An active color piece should be placed on the from-square of SAN"
MSG_OPPOSITE_FROM_SQUARE: Final[str] = "An active color piece should be placed on the from-square of SAN"
MSG_FULL_TO_SQUARE: Final[str] = "The to-square of SAN must be empty or place an inactive color piece"
MSG_INVALID_PIECE_MOVE: Final[
    str
] = "An piece located on the from-square of SAN cannot be moved to the to-square of SAN"
ERROR_TYPE_CANNOT_CASTLE: Final[str] = "movetarget.CannotCastleError"
ERROR_TYPE_EMPTY_FROM_SQUARE: Final[str] = "movetarget.EmptyFromSquareError"
ERROR_TYPE_OPPOSITE_FROM_SQUARE: Final[str] = "movetarget.OppositeFromSquareError"
ERROR_TYPE_FULL_TO_SQUARE: Final[str] = "movetarget.FullToSquareError"
ERROR_TYPE_INVALID_PIECE_MOVE: Final[str] = "movetarget.InvalidPieceMoveError"


class CannotCastle:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_CANNOT_CASTLE,
            location="body",
            param="fens, sans",
            value=[self.__fens, self.__sans],
            error=ERROR_TYPE_CANNOT_CASTLE,
        )


class EmptyFromSquare:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_EMPTY_FROM_SQUARE,
            location="body",
            param="fens, sans",
            value=[self.__fens, self.__sans],
            error=ERROR_TYPE_EMPTY_FROM_SQUARE,
        )


class OppositeFromSquare:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_OPPOSITE_FROM_SQUARE,
            location="body",
            param="fens, sans",
            value=[self.__fens, self.__sans],
            error=ERROR_TYPE_OPPOSITE_FROM_SQUARE,
        )


class FullToSquare:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_FULL_TO_SQUARE,
            location="body",
            param="fens, sans",
            value=[self.__fens, self.__sans],
            error=ERROR_TYPE_FULL_TO_SQUARE,
        )


class InvalidPieceMove:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_INVALID_PIECE_MOVE,
            location="body",
            param="fens, sans",
            value=[self.__fens, self.__sans],
            error=ERROR_TYPE_INVALID_PIECE_MOVE,
        )
