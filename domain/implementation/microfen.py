# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Dict, List, Optional, cast

from infra.rawboardstring import RawBoardString

from .boardstring import FEN, BoardString, ValidMicroBoardString
from .extendtype import Nullable
from .mirroredboardpart import MirroredBoardPart


class CreatedBoard:
    __slots__ = ["__board", "__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[RawBoardString]:
        board: RawBoardString = RawBoardString(str(self.__fen))

        return None if BoardString(board).empty() else board


class ValidBoardPartMicroFen:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[FEN]:
        return (
            Nullable(CreatedBoard(self.__fen).value())
            .op(lambda x: BoardString(cast(RawBoardString, x)))
            .op(lambda x: ValidMicroBoardString(x).value())
            .op(lambda x: None if x is None else self.__fen)
            .value()
        )


class SplitedMicroFen:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> List[str]:
        return self.__fen.split(" ")


class ValidCastlingPartMicroFen:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[FEN]:
        castling: str = SplitedMicroFen(self.__fen).value()[2]
        return None if ("Q" in castling or "q" in castling) else self.__fen


class ValidEnpassantPartMicroFen:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[FEN]:
        enpassant: str = SplitedMicroFen(self.__fen).value()[3]
        return self.__fen if enpassant == "-" else None


class ValidMicroFen:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> Optional[FEN]:
        return (
            Nullable(ValidBoardPartMicroFen(self.__fen).value())
            .op(lambda x: ValidCastlingPartMicroFen(cast(FEN, x)).value())
            .op(lambda x: ValidEnpassantPartMicroFen(cast(FEN, x)).value())
            .value()
        )


MIRRORED_CASTLING_PART: Dict[str, str] = {"Kk": "Kk", "K": "k", "k": "K", "-": "-"}
MIRRORED_TURN_PART: Dict[str, str] = {"w": "b", "b": "w"}


class MirroredMicroFen:
    __slots__ = ["__fen"]

    __fen: FEN

    def __init__(self, fen: FEN):
        self.__fen = fen

    def value(self) -> FEN:
        splited: List[str] = SplitedMicroFen(self.__fen).value()

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
