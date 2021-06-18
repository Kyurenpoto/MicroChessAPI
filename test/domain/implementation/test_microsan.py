# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from dependency_injector import providers
from src.config import Container
from src.domain.dto.modeldto import ModelAPIInfo
from src.domain.error.microsanerror import InvalidFromSquare, InvalidLength, InvalidPromotion, InvalidToSquare
from src.domain.implementation.basictype import SAN
from src.domain.implementation.microsan import MicroSAN, ValidMicroSAN


def test_normal() -> None:
    ValidMicroSAN.from_MicroSAN(MicroSAN.from_index_with_SANs(0, [SAN.first_move()])).san == SAN.first_move()


def test_castling() -> None:
    ValidMicroSAN.from_MicroSAN(MicroSAN.from_index_with_SANs(0, [SAN.castling()])).san == SAN.castling()


@pytest.mark.parametrize(
    "san",
    [
        (SAN("xx"),),
        (SAN("xxxxxx")),
    ],
)
def test_invalid_length(san: SAN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroSAN.from_MicroSAN(MicroSAN.from_index_with_SANs(0, [san]))

    assert exinfo.value.args[0].error == InvalidLength.error_type()


@pytest.mark.parametrize(
    "san",
    [
        (SAN("xxxx")),
        (SAN("xxxxx")),
        (SAN("a1e4")),
    ],
)
def test_invalid_from_square(san: SAN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroSAN.from_MicroSAN(MicroSAN.from_index_with_SANs(0, [san]))

    assert exinfo.value.args[0].error == InvalidFromSquare.error_type()


@pytest.mark.parametrize(
    "san",
    [
        (SAN("e4xx")),
        (SAN("e4xxx")),
        (SAN("e4a1")),
    ],
)
def test_invalid_to_square(san: SAN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroSAN.from_MicroSAN(MicroSAN.from_index_with_SANs(0, [san]))

    assert exinfo.value.args[0].error == InvalidToSquare.error_type()


@pytest.mark.parametrize(
    "san",
    [
        (SAN("e4e4x")),
    ],
)
def test_invalid_promotion(san: SAN, container: Container) -> None:
    container.api_info.override(providers.Factory(ModelAPIInfo, name="next-fen", method="post"))

    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroSAN.from_MicroSAN(MicroSAN.from_index_with_SANs(0, [san]))

    assert exinfo.value.args[0].error == InvalidPromotion.error_type()
