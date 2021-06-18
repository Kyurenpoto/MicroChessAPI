# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from dependency_injector import containers, providers

from src.domain.dto.modeldto import ModelAPIInfo, ModelInternal


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    internal_model = providers.Factory(ModelInternal, routes=config.routes)
    api_info = providers.Factory(ModelAPIInfo, name=config.name, method=config.method)


container = Container()
