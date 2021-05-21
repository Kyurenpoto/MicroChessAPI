# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Optional

import chess


class RawCheckedFEN(str):
    def checked(self) -> Optional[str]:
        return self if chess.Board(self).is_check() else None
