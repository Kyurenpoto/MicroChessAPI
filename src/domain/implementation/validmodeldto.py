# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from src.domain.dto.modeldto import ModelFENStatusRequest, ModelNextFENRequest
from src.domain.error.dtoerror import EmptyFENs, EmptySANs, NotMatchedNumberFENsSANs


class ValidModelNextFENRequest(ModelNextFENRequest):
    @classmethod
    def from_request(cls, request: ModelNextFENRequest) -> ValidModelNextFENRequest:
        return (
            ValidModelNextFENRequest(fens=request.fens, sans=request.sans)
            .not_empty_FENs()
            .not_empty_SANs()
            .matched_number_FENs_SANs()
        )

    def not_empty_FENs(self) -> ValidModelNextFENRequest:
        if len(self.fens) == 0:
            raise RuntimeError(EmptyFENs.from_FENs(self.fens))

        return self

    def not_empty_SANs(self) -> ValidModelNextFENRequest:
        if len(self.sans) == 0:
            raise RuntimeError(EmptySANs.from_SANs(self.sans))

        return self

    def matched_number_FENs_SANs(self) -> ValidModelNextFENRequest:
        if len(self.fens) != len(self.sans):
            raise RuntimeError(NotMatchedNumberFENsSANs.from_FENs_SANs(self.fens, self.sans))

        return self


class ValidModelFENStatusRequest(ModelFENStatusRequest):
    @classmethod
    def from_request(cls, request: ModelFENStatusRequest) -> ValidModelFENStatusRequest:
        return ValidModelFENStatusRequest(fens=request.fens).not_empty_FENs()

    def not_empty_FENs(self) -> ValidModelFENStatusRequest:
        if len(self.fens) == 0:
            raise RuntimeError(EmptyFENs.from_FENs(self.fens))

        return self
