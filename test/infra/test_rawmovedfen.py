# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from domain.error.microboarderror import (
    MSG_CANNOT_CASTLE,
    MSG_EMPTY_FROM_SQUARE,
    MSG_FULL_TO_SQUARE,
    MSG_INVALID_PIECE_MOVE,
    MSG_OPPOSITE_FROM_SQUARE,
)
from domain.implementation.microboard import (
    MICRO_BLACK_CASTLABLE_FEN,
    MICRO_BLACK_CASTLED_FEN,
    MICRO_FIRST_MOVE_FEN,
    MICRO_ONLY_KING_FEN,
    MICRO_STARTING_FEN,
    MICRO_SWAP_KING_BISHOP_FEN,
)
from domain.implementation.microsan import (
    MICRO_CASTLING_SAN,
    MICRO_FIRST_MOVE_SAN,
    MICRO_KING_SIDE_MOVE_SAN,
    MICRO_SECOND_MOVE_SAN,
)

from infra.rawmovedfen import RawMovedFen


def test_normal() -> None:
    assert str(RawMovedFen(MICRO_STARTING_FEN, MICRO_FIRST_MOVE_SAN)) == MICRO_FIRST_MOVE_FEN


def test_black_castling() -> None:
    assert str(RawMovedFen(MICRO_BLACK_CASTLABLE_FEN, MICRO_CASTLING_SAN)) == MICRO_BLACK_CASTLED_FEN


def test_cannot_castle() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        str(RawMovedFen(MICRO_STARTING_FEN, MICRO_CASTLING_SAN))

    assert exinfo.value.args[0] == MSG_CANNOT_CASTLE


def test_empty_from_square() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        str(RawMovedFen(MICRO_ONLY_KING_FEN, MICRO_FIRST_MOVE_SAN))

    assert exinfo.value.args[0] == MSG_EMPTY_FROM_SQUARE


def test_opposite_from_square() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        str(RawMovedFen(MICRO_STARTING_FEN, MICRO_SECOND_MOVE_SAN))

    assert exinfo.value.args[0] == MSG_OPPOSITE_FROM_SQUARE


def test_full_to_square() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        str(RawMovedFen(MICRO_STARTING_FEN, MICRO_KING_SIDE_MOVE_SAN))

    assert exinfo.value.args[0] == MSG_FULL_TO_SQUARE


def test_invalid_piece_move() -> None:
    with pytest.raises(RuntimeError) as exinfo:
        str(RawMovedFen(MICRO_SWAP_KING_BISHOP_FEN, MICRO_KING_SIDE_MOVE_SAN))

    assert exinfo.value.args[0] == MSG_INVALID_PIECE_MOVE
