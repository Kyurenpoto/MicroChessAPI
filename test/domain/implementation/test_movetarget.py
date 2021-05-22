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
from domain.implementation.basictype import FEN, SAN
from domain.implementation.movetarget import MoveTarget, ValidMoveTarget


def test_cannot_castle() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget(MoveTarget(0, [FEN.starting()], [SAN.castling()])).value()

    assert exinfo.value.args[0].error == CannotCastle.error_type()


def test_empty_from_square() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget(MoveTarget(0, [FEN.only_king()], [SAN.first_move()])).value()

    assert exinfo.value.args[0].error == EmptyFromSquare.error_type()


def test_opposite_from_square() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget(MoveTarget(0, [FEN.starting()], [SAN.second_move()])).value()

    assert exinfo.value.args[0].error == OppositeFromSquare.error_type()


def test_full_to_square() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget(MoveTarget(0, [FEN.starting()], [SAN.king_side_move()])).value()

    assert exinfo.value.args[0].error == FullToSquare.error_type()


def test_invalid_piece_move() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget(MoveTarget(0, [FEN.swap_king_bishop()], [SAN.king_side_move()])).value()

    assert exinfo.value.args[0].error == InvalidPieceMove.error_type()
