# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, Final, List, Union

MSG_EMPTY_FENS: Final[str] = "At least one FEN must be entered"
MSG_EMPTY_SANS: Final[str] = "At least one SAN must be entered"
MSG_NOT_MATCHED_NUMBER_FENS_SANS: Final[str] = "The number of FENs and the number of SANs do not matched"


class EmptyFENs:
    __slots__ = ["__fens"]

    __fens: List[str]

    def __init__(self, fens: List[str]):
        self.__fens = fens

    def value(self) -> Dict[str, Union[str, List[str]]]:
        return {
            "message": MSG_EMPTY_FENS,
            "location": "body",
            "param": "fens",
            "value": self.__fens,
            "error": "EmptyLengthError",
        }


class EmptySANs:
    __slots__ = ["__sans"]

    __sans: List[str]

    def __init__(self, sans: List[str]):
        self.__sans = sans

    def value(self) -> Dict[str, Union[str, List[str]]]:
        return {
            "message": MSG_EMPTY_SANS,
            "location": "body",
            "param": "sans",
            "value": self.__sans,
            "error": "EmptyLengthError",
        }


class NotMatchedNumberFENsSANs:
    __slots__ = ["__fens", "__sans"]

    __fens: List[str]
    __sans: List[str]

    def __init__(self, fens: List[str], sans: List[str]):
        self.__fens = fens
        self.__sans = sans

    def value(self) -> Dict[str, Union[str, List[List[str]]]]:
        return {
            "message": MSG_NOT_MATCHED_NUMBER_FENS_SANS,
            "location": "body",
            "param": "fens, sans",
            "value": [self.__fens, self.__sans],
            "error": "EmptyLengthError",
        }
