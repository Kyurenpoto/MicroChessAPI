# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

from fastapi.encoders import jsonable_encoder

from domain.dto.tests import Action, ActionResult, State
from domain.microchess import MicroBoardStatus

async def move(action: Action) -> Dict:
    result: ActionResult = ActionResult(fen="", status=MicroBoardStatus.NONE, next_move_list=[])
    return jsonable_encoder(result)

async def reset(state: State) -> Dict[str, bool]:
    return { "success": True }
