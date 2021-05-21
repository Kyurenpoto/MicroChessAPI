# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import NamedTuple

from .mirroredrow import MirroredRow

MIRRORED_PIECE: dict[str, str] = {
    "/": "/",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "P": "p",
    "p": "P",
    "K": "k",
    "k": "K",
    "Q": "q",
    "q": "Q",
    "R": "r",
    "r": "R",
    "N": "n",
    "n": "N",
    "B": "b",
    "b": "B",
}


class MirroredBoardPart(NamedTuple):
    boardpart: str

    def value(self) -> str:
        splited: list[str] = "".join(map(lambda x: MIRRORED_PIECE[x], self.boardpart)).split("/")

        return "/".join([MirroredRow(row).value() for row in splited[4::-1]] + splited[5:])
