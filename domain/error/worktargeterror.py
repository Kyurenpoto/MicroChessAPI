# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, Final, List, Union

NUMERAL: Dict[int, str] = {1: "st", 2: "nd", 3: "rd"}


def index_message(index: int) -> str:
    numeral: str = NUMERAL[index] if index in NUMERAL.keys() else "th"
    return f"At the {index}{numeral} element: "


MSG_CANNOT_CASTLE: Final[
    str
] = "Castling is only possible when FEN's castling availability is active and between king and rook is empty"
MSG_EMPTY_FROM_SQUARE: Final[str] = "An active color piece should be placed on the from-square of SAN"
MSG_OPPOSITE_FROM_SQUARE: Final[str] = "An active color piece should be placed on the from-square of SAN"
MSG_FULL_TO_SQUARE: Final[str] = "The to-square of SAN must be empty or place an inactive color piece"
MSG_INVALID_PIECE_MOVE: Final[
    str
] = "An piece located on the from-square of SAN cannot be moved to the to-square of SAN"


class CannotCastle:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> Dict[str, Union[str, List[List[str]]]]:
        return {
            "message": index_message(self.__index) + MSG_CANNOT_CASTLE,
            "location": "body",
            "param": "fens, sans",
            "value": [self.__fens, self.__sans],
            "error": "InvalidMoveContextError",
        }


class EmptyFromSquare:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> Dict[str, Union[str, List[List[str]]]]:
        return {
            "message": index_message(self.__index) + MSG_EMPTY_FROM_SQUARE,
            "location": "body",
            "param": "fens, sans",
            "value": [self.__fens, self.__sans],
            "error": "InvalidMoveContextError",
        }


class OppositeFromSquare:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> Dict[str, Union[str, List[List[str]]]]:
        return {
            "message": index_message(self.__index) + MSG_OPPOSITE_FROM_SQUARE,
            "location": "body",
            "param": "fens, sans",
            "value": [self.__fens, self.__sans],
            "error": "InvalidMoveContextError",
        }


class FullToSquare:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> Dict[str, Union[str, List[List[str]]]]:
        return {
            "message": index_message(self.__index) + MSG_FULL_TO_SQUARE,
            "location": "body",
            "param": "fens, sans",
            "value": [self.__fens, self.__sans],
            "error": "InvalidMoveContextError",
        }


class InvalidPieceMove:
    __slots__ = ["__index", "__fens", "__sans"]

    __index: int
    __fens: List[str]
    __sans: List[str]

    def __init__(self, index: int, fens: List[str], sans: List[str]):
        self.__index = index
        self.__fens = fens
        self.__sans = sans

    def value(self) -> Dict[str, Union[str, List[List[str]]]]:
        return {
            "message": index_message(self.__index) + MSG_INVALID_PIECE_MOVE,
            "location": "body",
            "param": "fens, sans",
            "value": [self.__fens, self.__sans],
            "error": "InvalidMoveContextError",
        }
