# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from fastapi import FastAPI

from presentation.api.modelapi import router

app: FastAPI = FastAPI()

app.include_router(router)
