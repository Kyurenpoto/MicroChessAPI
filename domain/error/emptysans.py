# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, Final, List, Union

MSG_EMPTY_SANS: Final[str] = "At least one SAN must be entered"


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
