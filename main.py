# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

import argparse

import uvicorn
from fastapi import FastAPI

import src.domain.error as error
import src.domain.model as model
from src.config import Container
from src.presentation.api.modelapi import router

app: FastAPI = FastAPI()

app.include_router(router)


def wire() -> None:
    app.state.container = Container()
    app.state.container.config.from_dict(
        {"routes": {route.name: route.path for route in router.routes}, "name": "", "method": ""}
    )
    app.state.container.wire(modules=[model], packages=[error])


def unwire() -> None:
    app.state.container.unwire()


def run() -> None:
    uvicorn.run("main:app", host="0.0.0.0", port=args.port)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MicroChess API Server")

    parser.add_argument("--port", type=int, default=8000, help="Port to bind socket of API server")

    args = parser.parse_args()

    wire()
    run()
