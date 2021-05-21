# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import NamedTuple


class IndexedFENsError(NamedTuple):
    index: int
    fens: list[str]


class IndexedSANsError(NamedTuple):
    index: int
    sans: list[str]


class IndexedParamsError(NamedTuple):
    index: int
    fens: list[str]
    sans: list[str]
