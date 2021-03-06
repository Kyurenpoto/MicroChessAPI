# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from dependency_injector import providers
from src.config import Container
from src.domain.dto.modeldto import ModelAPIInfo
from src.domain.error.movetargeterror import (
    CannotCastle,
    EmptyFromSquare,
    FullToSquare,
    InvalidPieceMove,
    OppositeFromSquare,
)
from src.domain.implementation.basictype import FEN, SAN
from src.domain.implementation.movetarget import MoveTarget, ValidMoveTarget


@pytest.mark.parametrize(
    "fen, san",
    [
        (FEN.starting(), SAN.first_move()),
        (FEN.black_castlable(), SAN.castling()),
        (FEN.white_castlable(), SAN.castling()),
    ],
)
def test_normal(fen: FEN, san: SAN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    target: MoveTarget = MoveTarget.from_index_with_FENs_SANs(0, [fen], [san])

    assert ValidMoveTarget.from_move_target(target) == target


def test_cannot_castle(container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget.from_move_target(MoveTarget.from_index_with_FENs_SANs(0, [FEN.starting()], [SAN.castling()]))

    assert exinfo.value.args[0].error == CannotCastle.error_type()


def test_empty_from_square(container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget.from_move_target(MoveTarget.from_index_with_FENs_SANs(0, [FEN.only_king()], [SAN.first_move()]))

    assert exinfo.value.args[0].error == EmptyFromSquare.error_type()


def test_opposite_from_square(container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget.from_move_target(MoveTarget.from_index_with_FENs_SANs(0, [FEN.starting()], [SAN.second_move()]))

    assert exinfo.value.args[0].error == OppositeFromSquare.error_type()


def test_full_to_square(container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget.from_move_target(
            MoveTarget.from_index_with_FENs_SANs(0, [FEN.starting()], [SAN.king_side_move()])
        )

    assert exinfo.value.args[0].error == FullToSquare.error_type()


def test_invalid_piece_move(container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMoveTarget.from_move_target(
            MoveTarget.from_index_with_FENs_SANs(0, [FEN.swap_king_bishop()], [SAN.king_side_move()])
        )

    assert exinfo.value.args[0].error == InvalidPieceMove.error_type()
