# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, List

from .basictype import FEN
from .mirroredboardpart import MirroredBoardPart


class MicroFEN:
    __slots__ = ["__index", "__fens", "__fen"]

    __index: int
    __fens: List[str]
    __fen: FEN

    def __init__(self, index: int, fens: List[str]):
        self.__index = index
        self.__fens = fens
        self.__fen = FEN("")

    def fen(self) -> FEN:
        if self.__fen == FEN(""):
            self.__fen = FEN(self.__fens[self.__index])

        return self.__fen

    def index(self) -> int:
        return self.__index

    def fens(self) -> List[str]:
        return self.__fens


MIRRORED_CASTLING_PART: Dict[str, str] = {"Kk": "Kk", "K": "k", "k": "K", "-": "-"}
MIRRORED_TURN_PART: Dict[str, str] = {"w": "b", "b": "w"}


class MirroredMicroFEN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> FEN:
        splited: List[str] = self.__fen.split(" ")

        return FEN(
            " ".join(
                [
                    MirroredBoardPart(splited[0]).value(),
                    MIRRORED_TURN_PART[splited[1]],
                    MIRRORED_CASTLING_PART[splited[2]],
                ]
                + splited[3:]
            )
        )
