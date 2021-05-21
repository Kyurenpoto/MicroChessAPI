# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import NamedTuple

from .mappable import Mappable

EXPAND_LEFT_SPACE: dict[str, str] = {
    "5": "41",
    "6": "42",
    "7": "43",
    "8": "44",
}


class ExpandedRow(NamedTuple):
    row: str

    def value(self) -> str:
        return self.row if self.row[0] == "4" else EXPAND_LEFT_SPACE[self.row[0]] + self.row[1:]


class PartialMirroredRow(NamedTuple):
    row: str

    def value(self) -> str:
        return self.row[0] + self.row[:0:-1]


SQUEEZE_LEFT_SPACE: dict[str, str] = {
    "4P": "4P",
    "4p": "4p",
    "4K": "4K",
    "4k": "4k",
    "4Q": "4Q",
    "4q": "4q",
    "4R": "4R",
    "4r": "4r",
    "4N": "4N",
    "4n": "4n",
    "4B": "4B",
    "4b": "4b",
    "41": "5",
    "42": "6",
    "43": "7",
}


class SqueezedRow(NamedTuple):
    row: str

    def value(self) -> str:
        return SQUEEZE_LEFT_SPACE[self.row[:2]] + self.row[2:]


class MirroredRow(NamedTuple):
    row: str

    def value(self) -> str:
        return (
            self.row
            if self.row == "8"
            else (
                Mappable(self.row)
                .mapped(lambda x: ExpandedRow(x).value())
                .mapped(lambda x: PartialMirroredRow(x).value())
                .mapped(lambda x: SqueezedRow(x).value())
                .value()
            )
        )
