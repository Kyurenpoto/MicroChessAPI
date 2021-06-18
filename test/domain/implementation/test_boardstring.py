# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from dependency_injector import providers
from src.config import Container
from src.domain.dto.modeldto import ModelAPIInfo
from src.domain.error.boardstringerror import InvalidPieceNumber, NotEmptyOutside
from src.domain.implementation.basictype import FEN
from src.domain.implementation.microfen import MicroFEN
from src.domain.implementation.validmicrofen import ValidMicroFEN


@pytest.mark.parametrize(
    "fen",
    [
        (FEN("r3knbr/4p3/8/7P/4RBNK/8/8/8 w Kk - 0 1")),
        (FEN("4knbr/4p3/8/7P/4RBNK/8/8/7r w Kk - 0 1")),
    ],
)
def test_not_empty_outside(fen: FEN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen]))

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
def test_invalid_piece_number(fen: FEN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroFEN.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen]))

    assert exinfo.value.args[0].error == InvalidPieceNumber.error_type()
