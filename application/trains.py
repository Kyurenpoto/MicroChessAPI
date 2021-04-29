# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict

from fastapi.encoders import jsonable_encoder

from domain.dto.trains import Action, ActionResult, State

async def move(action: Action) -> Dict:
    result: ActionResult = ActionResult(fens=[], statuses=[], next_move_lists=[])
    return jsonable_encoder(result)

async def reset(state: State) -> Dict[str, bool]:
    return { "success": True }
