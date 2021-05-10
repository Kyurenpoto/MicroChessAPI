# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, List

from .boardstring import FEN, BoardString, ValidMicroBoardString
from .mappable import Mappable
from .mirroredboardpart import MirroredBoardPart


class ValidBoardPartMicroFEN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> FEN:
        return ValidMicroBoardString(BoardString(self.__fen)).value().fen()


class SplitedMicroFEN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> List[str]:
        return self.__fen.split(" ")


class ValidCastlingPartMicroFEN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> FEN:
        castling: str = SplitedMicroFEN(self.__fen).value()[2]
        if "Q" in castling or "q" in castling:
            raise RuntimeError("Invalid castling part")

        return self.__fen


class ValidEnpassantPartMicroFEN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> FEN:
        if SplitedMicroFEN(self.__fen).value()[3] != "-":
            raise RuntimeError("Invalid enpassant part")

        return self.__fen


class ValidMicroFEN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> FEN:
        return (
            Mappable(ValidBoardPartMicroFEN(self.__fen).value())
            .mapped(lambda x: ValidCastlingPartMicroFEN(x).value())
            .mapped(lambda x: ValidEnpassantPartMicroFEN(x).value())
            .value()
        )


MIRRORED_CASTLING_PART: Dict[str, str] = {"Kk": "Kk", "K": "k", "k": "K", "-": "-"}
MIRRORED_TURN_PART: Dict[str, str] = {"w": "b", "b": "w"}


class MirroredMicroFEN:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> FEN:
        splited: List[str] = SplitedMicroFEN(self.__fen).value()

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
