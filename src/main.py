# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from fastapi import FastAPI

from src.presentation.api.modelapi import router

app: FastAPI = FastAPI()

app.include_router(router)

import argparse

import uvicorn

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MicroChess API Server")

    parser.add_argument("--port", type=int, default=8000, help="Port to bind socket of API server")

    args = parser.parse_args()

    uvicorn.run("main:app", host="0.0.0.0", port=args.port)
