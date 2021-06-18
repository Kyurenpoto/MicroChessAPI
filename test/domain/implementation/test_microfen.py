# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from dependency_injector import providers
from src.config import Container
from src.domain.dto.modeldto import ModelAPIInfo
from src.domain.error.microfenerror import (
    InvalidCastlingPart,
    InvalidEnpassantPart,
    InvalidFullmovePart,
    InvalidHalfmovePart,
    InvalidStructure,
    InvalidTurnPart,
)
from src.domain.implementation.basictype import FEN
from src.domain.implementation.microfen import MicroFEN
from src.domain.implementation.validmicrofen import ValidMicroFEN


@pytest.mark.parametrize(
    "fen",
    [
        (FEN.starting()),
        (FEN.white_castlable()),
        (FEN.black_castlable()),
    ],
)
def test_normal(fen: FEN) -> None:
    ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen])).fen == fen


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1 ")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1 x")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0")),
    ],
)
def test_invalid_structure(fen: FEN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen]))

    assert exinfo.value.args[0].error == InvalidStructure.error_type()


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8  Kk - 0 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 x Kk - 0 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 W Kk - 0 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 B Kk - 0 1")),
    ],
)
def test_invalid_turn_part(fen: FEN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen]))

    assert exinfo.value.args[0].error == InvalidTurnPart.error_type()


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Q - 0 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w q - 0 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w x - 0 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w kK - 0 1")),
    ],
)
def test_invalid_castling_part(fen: FEN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen]))

    assert exinfo.value.args[0].error == InvalidCastlingPart.error_type()


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk x 0 1")),
        (FEN("4knbr/4p2P/8/8/4RBNK/8/8/8 b Kk h5 0 1")),
    ],
)
def test_invalid_enpassant_part(fen: FEN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen]))

    assert exinfo.value.args[0].error == InvalidEnpassantPart.error_type()


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk -  1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - x 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - -1 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 51 1")),
    ],
)
def test_invalid_halfmove_part(fen: FEN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen]))

    assert exinfo.value.args[0].error == InvalidHalfmovePart.error_type()


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 ")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 x")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 0")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 -1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 81")),
    ],
)
def test_invalid_fullmove_part(fen: FEN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen]))

    assert exinfo.value.args[0].error == InvalidFullmovePart.error_type()
