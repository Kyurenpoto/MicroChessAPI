# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from domain.dto.modeldto import ModelErrorResponse


class EmptyFENs:
    @classmethod
    def msg(cls) -> str:
        return "At least one FEN must be entered"

    @classmethod
    def error_type(cls) -> str:
        return "modeldto.EmptyFENsError"

    @classmethod
    def from_FENs(cls, fens: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=EmptyFENs.msg(), location="body", param="fens", value=fens, error=EmptyFENs.error_type()
        )


class EmptySANs:
    @classmethod
    def msg(cls) -> str:
        return "At least one SAN must be entered"

    @classmethod
    def error_type(cls) -> str:
        return "modeldto.EmptySANsError"

    @classmethod
    def from_SANs(cls, sans: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=EmptySANs.msg(), location="body", param="sans", value=sans, error=EmptySANs.error_type()
        )


class NotMatchedNumberFENsSANs:
    @classmethod
    def msg(cls) -> str:
        return "The number of FENs and the number of SANs must be the same"

    @classmethod
    def error_type(cls) -> str:
        return "modeldto.NotMatchedNumberFENsSANsError"

    @classmethod
    def from_FENs_SANs(cls, fens: list[str], sans: list[str]) -> ModelErrorResponse:
        return ModelErrorResponse(
            message=NotMatchedNumberFENsSANs.msg(),
            location="body",
            param="fens, sans",
            value=[fens, sans],
            error=NotMatchedNumberFENsSANs.error_type(),
        )
