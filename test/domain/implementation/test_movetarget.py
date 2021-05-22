# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from domain.error.movetargeterror import (
    CannotCastle,
    EmptyFromSquare,
    FullToSquare,
    InvalidPieceMove,
    OppositeFromSquare,
)
from domain.implementation.basictype import FEN
from domain.implementation.movetarget import MoveTarget, ValidMoveTarget
from domain.implementation.validmicrosan import (
    MICRO_CASTLING_SAN,
    MICRO_FIRST_MOVE_SAN,
    MICRO_KING_SIDE_MOVE_SAN,
    MICRO_SECOND_MOVE_SAN,
)


def test_cannot_castle() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget(MoveTarget(0, [FEN.starting()], [MICRO_CASTLING_SAN])).value()

    assert exinfo.value.args[0].error == CannotCastle.error_type()


def test_empty_from_square() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget(MoveTarget(0, [FEN.only_king()], [MICRO_FIRST_MOVE_SAN])).value()

    assert exinfo.value.args[0].error == EmptyFromSquare.error_type()


def test_opposite_from_square() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget(MoveTarget(0, [FEN.starting()], [MICRO_SECOND_MOVE_SAN])).value()

    assert exinfo.value.args[0].error == OppositeFromSquare.error_type()


def test_full_to_square() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget(MoveTarget(0, [FEN.starting()], [MICRO_KING_SIDE_MOVE_SAN])).value()

    assert exinfo.value.args[0].error == FullToSquare.error_type()


def test_invalid_piece_move() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget(MoveTarget(0, [FEN.swap_king_bishop()], [MICRO_KING_SIDE_MOVE_SAN])).value()

    assert exinfo.value.args[0].error == InvalidPieceMove.error_type()
