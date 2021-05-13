# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import pytest
from domain.error.microsanerror import (
    ERROR_TYPE_INVALID_FROM_SQUARE,
    ERROR_TYPE_INVALID_LENGTH,
    ERROR_TYPE_INVALID_PROMOTION,
    ERROR_TYPE_INVALID_TO_SQUARE,
)
from domain.implementation.basictype import SAN
from domain.implementation.microsan import MicroSAN
from domain.implementation.validmicrosan import MICRO_CASTLING_SAN, MICRO_FIRST_MOVE_SAN, ValidMicroSAN


def test_normal() -> None:
    ValidMicroSAN(MicroSAN(0, [MICRO_FIRST_MOVE_SAN])).value().san() == MICRO_FIRST_MOVE_SAN


def test_castling() -> None:
    ValidMicroSAN(MicroSAN(0, [MICRO_CASTLING_SAN])).value().san() == MICRO_CASTLING_SAN


@pytest.mark.parametrize(
    "san",
    [
        (SAN("xx"),),
        (SAN("xxxxxx")),
    ],
)
def test_invalid_length(san: SAN) -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroSAN(MicroSAN(0, [san])).value()

    assert exinfo.value.args[0].error == ERROR_TYPE_INVALID_LENGTH


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
        ValidMicroSAN(MicroSAN(0, [san])).value()

    assert exinfo.value.args[0].error == ERROR_TYPE_INVALID_FROM_SQUARE


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
        ValidMicroSAN(MicroSAN(0, [san])).value()

    assert exinfo.value.args[0].error == ERROR_TYPE_INVALID_TO_SQUARE


@pytest.mark.parametrize(
    "san",
    [
        (SAN("e4e4x")),
    ],
)
def test_invalid_promotion(san: SAN) -> None:
    with pytest.raises(RuntimeError) as exinfo:
        ValidMicroSAN(MicroSAN(0, [san])).value()

    assert exinfo.value.args[0].error == ERROR_TYPE_INVALID_PROMOTION
