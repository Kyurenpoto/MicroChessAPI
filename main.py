# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from fastapi import FastAPI

from presentation import tests, trains

app: FastAPI = FastAPI()

app.include_router(tests.router)
app.include_router(trains.router)
