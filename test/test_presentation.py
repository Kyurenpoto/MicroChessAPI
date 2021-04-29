# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from fastapi import status
from fastapi.testclient import TestClient

from main import app

client: TestClient = TestClient(app)

def test_tests_action():
    response = client.put(url="/tests/action", json={"fen": "", "move": ""})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"fen": "", "status": 0, "next_move_list": []}

def test_trains_action():
    response = client.put(url="/trains/action", json={"fens": [], "moves": []})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"fens": [], "statuses": [], "next_move_lists": []}

def test_tests_state():
    response = client.post(url="/tests/state", json={"fen": ""})
    assert response.status_code == status.HTTP_201_CREATED

def test_trains_state():
    response = client.post(url="/trains/state", json={"fens": []})
    assert response.status_code == status.HTTP_201_CREATED
