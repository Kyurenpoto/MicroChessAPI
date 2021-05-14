# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, List

from domain.dto.modeldto import ModelErrorResponse
from domain.implementation.indexmessage import IndexMessage

MSG_INVALID_SYMBOL: Final[
    str
] = "The board part of the FEN should contain only the numbers 1~8, '/', and symbols representing chess pieces"
MSG_INVALID_ROW_NUMBER: Final[
    str
] = "The board part of the FEN should contain only The board part of FEN should have 8 rows separated by '/'"
MSG_INVALID_SQUARE_NUMBER: Final[
    str
] = "Each row in the board part of FEN should contain 8 squares, including a blank and a piece"
MSG_NOT_EMPTY_OUTSIDE: Final[str] = "All outside the MicroChess area in the board part of FEN should be blank"
MSG_INVALID_PIECE_NUMBER: Final[
    str
] = "Only one King, a maximum of 1 Queen and Pawn, and a maximum of 2 Rooks, Bishops, and Nights should exist in the board part"
ERROR_TYPE_INVALID_SYMBOL: Final[str] = "boardstring.InvalidSymbolError"
ERROR_TYPE_INVALID_ROW_NUMBER: Final[str] = "boardstring.InvalidRowNumberError"
ERROR_TYPE_INVALID_SQUARE_NUMBER: Final[str] = "boardstring.InvalidSquareNumberError"
ERROR_TYPE_NOT_EMPTY_OUTSIDE: Final[str] = "boardstring.NotEmptyOutsideError"
ERROR_TYPE_INVALID_PIECE_NUMBER: Final[str] = "boardstring.InvalidPieceNumberError"


class InvalidSymbol:
    __slots__ = ["__index", "__fens"]

    __index: int
    __fens: List[str]

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_INVALID_SYMBOL,
            location="body",
            param="fens",
            value=self.__fens,
            error=ERROR_TYPE_INVALID_SYMBOL,
        )


class InvalidRowNumber:
    __slots__ = ["__index", "__fens"]

    __index: int
    __fens: List[str]

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_INVALID_ROW_NUMBER,
            location="body",
            param="fens",
            value=self.__fens,
            error=ERROR_TYPE_INVALID_ROW_NUMBER,
        )


class InvalidSquareNumber:
    __slots__ = ["__index", "__fens"]

    __index: int
    __fens: List[str]

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_INVALID_SQUARE_NUMBER,
            location="body",
            param="fens",
            value=self.__fens,
            error=ERROR_TYPE_INVALID_SQUARE_NUMBER,
        )


class NotEmptyOutside:
    __slots__ = ["__index", "__fens"]

    __index: int
    __fens: List[str]

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_NOT_EMPTY_OUTSIDE,
            location="body",
            param="fens",
            value=self.__fens,
            error=ERROR_TYPE_NOT_EMPTY_OUTSIDE,
        )


class InvalidPieceNumber:
    __slots__ = ["__index", "__fens"]

    __index: int
    __fens: List[str]

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_INVALID_PIECE_NUMBER,
            location="body",
            param="fens",
            value=self.__fens,
            error=ERROR_TYPE_INVALID_PIECE_NUMBER,
        )
