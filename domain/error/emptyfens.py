# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, Final, List, Union

MSG_EMPTY_FENS: Final[str] = "At least one FEN must be entered"


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
