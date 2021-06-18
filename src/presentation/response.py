# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from typing import NamedTuple

from src.application.createdresponse import ICreatedResponse
from submodules.fastapi_haljson.src.halresponse import HALJSONResponse, OkResponse, UnprocessableEntityResponse


class ExceptionHandledResponse(NamedTuple):
    created: ICreatedResponse

    def handled(self) -> HALJSONResponse:
        try:
            return OkResponse.from_response_data(self.created.created())
        except RuntimeError as ex:
            return UnprocessableEntityResponse.from_response_data(ex.args[0])
