# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from domain.error.microsanerror import InvalidFromSquare, InvalidLength, InvalidPromotion, InvalidToSquare
from domain.implementation.basictype import SAN
from domain.implementation.microsan import MicroSAN
from domain.implementation.validmicrosan import ValidMicroSAN


def test_normal() -> None:
    ValidMicroSAN.from_MicroSAN(MicroSAN(0, [SAN.first_move()])).san() == SAN.first_move()


def test_castling() -> None:
    ValidMicroSAN.from_MicroSAN(MicroSAN(0, [SAN.castling()])).san() == SAN.castling()


@pytest.mark.parametrize(
    "san",
    [
        (SAN("xx"),),
        (SAN("xxxxxx")),
    ],
)
def test_invalid_length(san: SAN) -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroSAN.from_MicroSAN(MicroSAN(0, [san]))

    assert exinfo.value.args[0].error == InvalidLength.error_type()


@pytest.mark.parametrize(
    "san",
    [
        (SAN("xxxx")),
        (SAN("xxxxx")),
        (SAN("a1e4")),
    ],
)
def test_invalid_from_square(san: SAN) -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroSAN.from_MicroSAN(MicroSAN(0, [san]))

    assert exinfo.value.args[0].error == InvalidFromSquare.error_type()


@pytest.mark.parametrize(
    "san",
    [
        (SAN("e4xx")),
        (SAN("e4xxx")),
        (SAN("e4a1")),
    ],
)
def test_invalid_to_square(san: SAN) -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroSAN.from_MicroSAN(MicroSAN(0, [san]))

    assert exinfo.value.args[0].error == InvalidToSquare.error_type()


@pytest.mark.parametrize(
    "san",
    [
        (SAN("e4e4x")),
    ],
)
def test_invalid_promotion(san: SAN) -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroSAN.from_MicroSAN(MicroSAN(0, [san]))

    assert exinfo.value.args[0].error == InvalidPromotion.error_type()
