# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, Final, List, Union

MSG_NOT_MATCHED_NUMBER_FENS_SANS: Final[str] = "The number of FENs and the number of SANs do not matched"


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
