# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, NamedTuple

from domain.dto.modeldto import ModelErrorResponse

MSG_EMPTY_FENS: Final[str] = "At least one FEN must be entered"
MSG_EMPTY_SANS: Final[str] = "At least one SAN must be entered"
MSG_NOT_MATCHED_NUMBER_FENS_SANS: Final[str] = "The number of FENs and the number of SANs must be the same"
ERROR_TYPE_EMPTY_FENS: Final[str] = "modeldto.EmptyFENsError"
ERROR_TYPE_EMPTY_SANS: Final[str] = "modeldto.EmptySANsError"
ERROR_TYPE_NOT_MATCHED_NUMBER_FENS_SANS: Final[str] = "modeldto.NotMatchedNumberFENsSANsError"


class EmptyFENs(NamedTuple):
    fens: list[str]

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=MSG_EMPTY_FENS, location="body", param="fens", value=self.fens, error=ERROR_TYPE_EMPTY_FENS
        )


class EmptySANs(NamedTuple):
    sans: list[str]

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=MSG_EMPTY_SANS, location="body", param="sans", value=self.sans, error=ERROR_TYPE_EMPTY_SANS
        )


class NotMatchedNumberFENsSANs(NamedTuple):
    fens: list[str]
    sans: list[str]

    def value(self) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=MSG_NOT_MATCHED_NUMBER_FENS_SANS,
            location="body",
            param="fens, sans",
            value=[self.fens, self.sans],
            error=ERROR_TYPE_NOT_MATCHED_NUMBER_FENS_SANS,
        )
