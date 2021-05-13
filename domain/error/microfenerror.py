# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, List

from domain.dto.modeldto import ModelErrorResponse
from domain.implementation.indexmessage import IndexMessage

MSG_INVALID_STRUCTURE: Final[str] = (
    "The FEN should consist of 6 parts separated by spaces: "
    + "'[Board part] [Turn part] [Castling part] [Enpassant part] [Halfmove part] [Fullmove part]'"
)
MSG_INVALID_TURN_PART: Final[str] = "Turn part of FEN should be one of 'w', 'b'"
MSG_INVALID_CASTLING_PART: Final[str] = "Castling part of FEN should be one of 'Kk', 'K', 'k', or '-'"
MSG_INVALID_ENPASSANT_PART: Final[str] = "Enpassant part of FEN should be '-'"
MSG_INVALID_HALFMOVE_PART: Final[str] = "Halfmove part of FEN should be an integer in range [0, 50)"
MSG_INVALID_FULLMOVE_PART: Final[str] = "Fullmove part of FEN should be an integer in range [1, 80]"
ERROR_TYPE_INVALID_STRUCTURE: Final[str] = "microfen.InvalidStructureError"
ERROR_TYPE_INVALID_TURN_PART: Final[str] = "microfen.InvalidTurnPartError"
ERROR_TYPE_INVALID_CASTLING_PART: Final[str] = "microfen.InvalidCastlingPartError"
ERROR_TYPE_INVALID_ENPASSANT_PART: Final[str] = "microfen.InvalidEnpassantPartError"
ERROR_TYPE_INVALID_HALFMOVE_PART: Final[str] = "microfen.InvalidHalfmovePartError"
ERROR_TYPE_INVALID_FULLMOVE_PART: Final[str] = "microfen.InvalidFullmovePartError"


class InvalidStructure:
    __slots__ = ["__index", "__fens"]

    __index: int
    __fens: List[str]

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_INVALID_STRUCTURE,
            location="body",
            param="fens",
            value=self.__fens,
            error=ERROR_TYPE_INVALID_STRUCTURE,
        )


class InvalidTurnPart:
    __slots__ = ["__index", "__fens"]

    __index: int
    __fens: List[str]

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_INVALID_TURN_PART,
            location="body",
            param="fens",
            value=self.__fens,
            error=ERROR_TYPE_INVALID_TURN_PART,
        )


class InvalidCastlingPart:
    __slots__ = ["__index", "__fens"]

    __index: int
    __fens: List[str]

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_INVALID_CASTLING_PART,
            location="body",
            param="fens",
            value=self.__fens,
            error=ERROR_TYPE_INVALID_CASTLING_PART,
        )


class InvalidEnpassantPart:
    __slots__ = ["__index", "__fens"]

    __index: int
    __fens: List[str]

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_INVALID_ENPASSANT_PART,
            location="body",
            param="fens",
            value=self.__fens,
            error=ERROR_TYPE_INVALID_ENPASSANT_PART,
        )


class InvalidHalfmovePart:
    __slots__ = ["__index", "__fens"]

    __index: int
    __fens: List[str]

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_INVALID_HALFMOVE_PART,
            location="body",
            param="fens",
            value=self.__fens,
            error=ERROR_TYPE_INVALID_HALFMOVE_PART,
        )


class InvalidFullmovePart:
    __slots__ = ["__index", "__fens"]

    __index: int
    __fens: List[str]

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=IndexMessage(self.__index).value() + MSG_INVALID_FULLMOVE_PART,
            location="body",
            param="fens",
            value=self.__fens,
            error=ERROR_TYPE_INVALID_FULLMOVE_PART,
        )
