# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from fastapi import FastAPI

from presentation.api import testapi, trainapi, modelapi

app: FastAPI = FastAPI()

app.include_router(testapi.router)
app.include_router(trainapi.router)
app.include_router(modelapi.router)
