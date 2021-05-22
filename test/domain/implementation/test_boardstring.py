# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from domain.error.boardstringerror import (
    InvalidPieceNumber,
    InvalidRowNumber,
    InvalidSquareNumber,
    InvalidSymbol,
    NotEmptyOutside,
)
from domain.implementation.basictype import FEN
from domain.implementation.boardstring import BoardString, valid_micro_board_string
from domain.implementation.microfen import MicroFEN
from domain.implementation.validmicrofen import ValidMicroFEN


def test_normal() -> None:
    valid_micro_board_string(BoardString(MicroFEN(0, [FEN.starting()]))).fen().fen() == FEN.starting()
    valid_micro_board_string(BoardString(MicroFEN(0, [FEN.white_castlable()]))).fen().fen() == FEN.white_castlable()
    valid_micro_board_string(BoardString(MicroFEN(0, [FEN.black_castlable()]))).fen().fen() == FEN.black_castlable()


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4knbrx/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr./4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr?/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr0/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr9/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
    ],
)
def test_invalid_symbol(fen: FEN) -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN(0, [fen]))

    assert exinfo.value.args[0].error == InvalidSymbol.error_type()


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8/ w Kk - 0 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8 w Kk - 0 1")),
    ],
)
def test_invalid_row_number(fen: FEN) -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN(0, [fen]))

    assert exinfo.value.args[0].error == InvalidRowNumber.error_type()


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4knbrr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knb/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/1/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("5knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
    ],
)
def test_invalid_square_number(fen: FEN) -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN(0, [fen]))

    assert exinfo.value.args[0].error == InvalidSquareNumber.error_type()


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("r3knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/7r w Kk - 0 1")),
    ],
)
def test_not_empty_outside(fen: FEN) -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN(0, [fen]))

    assert exinfo.value.args[0].error == NotEmptyOutside.error_type()


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4knbr/4p2k/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p2p/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p2q/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p2r/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p2n/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p2b/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/6qq/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/6rr/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/6nn/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/6bb/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("5nbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/4k2P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/4P2P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/4Q2P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/4R2P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/4N2P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/4B2P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/4QQ2/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/4RR2/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/4NN2/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/4BB2/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/7P/4RBN1/8/8/8 w Kk - 0 1")),
    ],
)
def test_invalid_piece_number(fen: FEN) -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN(0, [fen]))

    assert exinfo.value.args[0].error == InvalidPieceNumber.error_type()
