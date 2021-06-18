# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only


from typing import NamedTuple, Union

from dependency_injector.wiring import Provide, inject
from src.config import Container
from src.domain.dto.modeldto import ModelAPIInfo, ModelErrorResponse, ModelInternal
from submodules.fastapi_haljson.src.halmodel import HALBase


class CreatedErrorResponse(NamedTuple):
    message: str
    param: str
    value: Union[list[str], list[list[str]]]
    error: str

    @inject
    def created(
        self,
        internal_model: ModelInternal = Provide[Container.internal_model],
        api_info: ModelAPIInfo = Provide[Container.api_info],
    ) -> ModelErrorResponse:
        return ModelErrorResponse(
            # links=HALBase.from_routes_with_requested(internal_model.routes, api_info.name, api_info.method).links,
            message=self.message,
            location="body",
            param=self.param,
            value=self.value,
            error=self.error,
        )
