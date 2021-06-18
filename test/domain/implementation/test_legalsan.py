# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from dependency_injector import providers
from src.config import Container
from src.domain.dto.modeldto import ModelAPIInfo
from src.domain.implementation.basictype import FEN
from src.domain.implementation.legalsan import LegalSANs


def test_normal(container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    assert LegalSANs.from_FEN(FEN.starting()) == LegalSANs.initial()


def test_checkmate(container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    assert LegalSANs.from_FEN(FEN.checkmate()) == []


def test_stalemate(container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    assert LegalSANs.from_FEN(FEN.stalemate()) == []


def test_black_castlable(container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    assert LegalSANs.from_FEN(FEN.black_castlable()) == LegalSANs.black_castable()


def test_white_castlable(container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    assert LegalSANs.from_FEN(FEN.white_castlable()) == LegalSANs.white_castable()
