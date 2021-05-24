# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from domain.implementation.movablefen import MovableFEN
from domain.implementation.movetarget import MoveTarget, ValidMoveTarget


class NextFen(str):
    @classmethod
    def from_index_with_FENs_SANs(cls, index: int, fens: list[str], sans: list[str]) -> NextFen:
        target: MoveTarget = ValidMoveTarget.from_move_target(MoveTarget.from_index_with_FENs_SANs(index, fens, sans))

        return NextFen(MovableFEN(target.fen).moved(target.san))


class ModelNextFENResult(list[str]):
    @classmethod
    def from_FENs_SANs(cls, fens: list[str], sans: list[str]) -> ModelNextFENResult:
        return ModelNextFENResult([NextFen.from_index_with_FENs_SANs(index, fens, sans) for index in range(len(fens))])
