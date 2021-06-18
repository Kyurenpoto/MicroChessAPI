# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from src.domain.error.createderror import CreatedErrorResponse


class EmptyFENs(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "modeldto.EmptyFENsError"

    @classmethod
    def from_FENs(cls, fens: list[str]) -> EmptyFENs:
        return EmptyFENs(
            "At least one FEN must be entered",
            "fens",
            fens,
            EmptyFENs.error_type(),
        )


class EmptySANs(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "modeldto.EmptySANsError"

    @classmethod
    def from_SANs(cls, sans: list[str]) -> EmptySANs:
        return EmptySANs(
            "At least one SAN must be entered",
            "sans",
            sans,
            EmptySANs.error_type(),
        )


class NotMatchedNumberFENsSANs(CreatedErrorResponse):
    @classmethod
    def error_type(cls) -> str:
        return "modeldto.NotMatchedNumberFENsSANsError"

    @classmethod
    def from_FENs_SANs(cls, fens: list[str], sans: list[str]) -> NotMatchedNumberFENsSANs:
        return NotMatchedNumberFENsSANs(
            "The number of FENs and the number of SANs must be the same",
            "fens, sans",
            [fens, sans],
            NotMatchedNumberFENsSANs.error_type(),
        )
