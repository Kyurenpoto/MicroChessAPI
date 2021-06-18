# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from dependency_injector import providers
from src.config import Container
from src.domain.dto.modeldto import ModelAPIInfo
from src.domain.error.boardparterror import InvalidRowNumber, InvalidSquareNumber, InvalidSymbol
from src.domain.implementation.basictype import FEN
from src.domain.implementation.microfen import MicroFEN
from src.domain.implementation.validmicrofen import ValidMicroFEN


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
def test_invalid_symbol(fen: FEN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen]))

    assert exinfo.value.args[0].error == InvalidSymbol.error_type()


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/8/ w Kk - 0 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8 w Kk - 0 1")),
    ],
)
def test_invalid_row_number(fen: FEN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen]))

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
def test_invalid_square_number(fen: FEN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen]))

    assert exinfo.value.args[0].error == InvalidSquareNumber.error_type()
