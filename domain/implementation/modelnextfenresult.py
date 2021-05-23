# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import NamedTuple

from domain.implementation.movablefen import MovableFEN
from domain.implementation.movetarget import MoveTarget, ValidMoveTarget


class NextFen(NamedTuple):
    index: int
    fens: list[str]
    sans: list[str]

    def value(self) -> str:
        target: MoveTarget = ValidMoveTarget(MoveTarget(self.index, self.fens, self.sans)).value()

        return MovableFEN(target.fen()).moved(target.san())


class ModelNextFENResult(NamedTuple):
    fens: list[str]
    sans: list[str]

    def value(self) -> list[str]:
        return [NextFen(index, self.fens, self.sans).value() for index in range(len(self.fens))]
