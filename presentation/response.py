# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from typing import NamedTuple

from application.createdresponse import ICreatedResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


class HALJSONResponse(JSONResponse):
    media_type = "application/hal+json"


class OkResponse(HALJSONResponse):
    @classmethod
    def from_response_data(cls, data) -> OkResponse:
        return OkResponse(content=jsonable_encoder(data))


class UnprocessableEntityResponse(HALJSONResponse):
    @classmethod
    def from_response_data(cls, data) -> UnprocessableEntityResponse:
        return UnprocessableEntityResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder(data)
        )


class ExceptionHandledResponse(NamedTuple):
    created: ICreatedResponse

    def handled(self) -> HALJSONResponse:
        try:
            return OkResponse.from_response_data(self.created.created())
        except RuntimeError as ex:
            return UnprocessableEntityResponse.from_response_data(ex.args[0])
