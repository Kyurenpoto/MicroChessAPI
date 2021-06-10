# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from typing import NamedTuple

from src.domain.implementation.microfen import MicroFEN


class SplitedFEN(list[str]):
    @classmethod
    def from_FEN(cls, fen: str) -> SplitedFEN:
        return SplitedFEN(fen.split(" "))

    def join_parts(self) -> str:
        return " ".join(self)


class FromBoardToColorParts(SplitedFEN):
    @classmethod
    def from_SplitedFEN(cls, splited: SplitedFEN) -> FromBoardToColorParts:
        return FromBoardToColorParts(splited[:2])


class FromEnpassantToFullmoveParts(SplitedFEN):
    @classmethod
    def from_SplitedFEN(cls, splited: SplitedFEN) -> FromEnpassantToFullmoveParts:
        return FromEnpassantToFullmoveParts(splited[3:])


class FromBoardToHalfmoveParts(SplitedFEN):
    @classmethod
    def from_SplitedFEN(cls, splited: SplitedFEN) -> FromBoardToHalfmoveParts:
        return FromBoardToHalfmoveParts(splited[:-1])


class BoardPart(NamedTuple):
    fen: MicroFEN
    board: str

    @classmethod
    def from_MicroFEN(cls, microfen: MicroFEN) -> BoardPart:
        return BoardPart(microfen, SplitedFEN.from_FEN(microfen.fen)[0])


class ColorPart(str):
    @classmethod
    def from_SplitedFEN(cls, splited: SplitedFEN) -> ColorPart:
        return ColorPart(splited[1])

    @classmethod
    def from_FEN(cls, fen: str) -> ColorPart:
        return ColorPart.from_SplitedFEN(SplitedFEN.from_FEN(fen))

    def mirror(self) -> ColorPart:
        return ColorPart({"w": "b", "b": "w"}[self])


class CastlingPart(str):
    @classmethod
    def from_SplitedFEN(cls, splited: SplitedFEN) -> CastlingPart:
        return CastlingPart(splited[2])

    @classmethod
    def from_FEN(cls, fen: str) -> CastlingPart:
        return CastlingPart.from_SplitedFEN(SplitedFEN.from_FEN(fen))


class EnpassantPart(str):
    @classmethod
    def from_SplitedFEN(cls, splited: SplitedFEN) -> EnpassantPart:
        return EnpassantPart(splited[3])

    @classmethod
    def from_FEN(cls, fen: str) -> EnpassantPart:
        return EnpassantPart.from_SplitedFEN(SplitedFEN.from_FEN(fen))


class RawHalfmovePart(str):
    @classmethod
    def from_SplitedFEN(cls, splited: SplitedFEN) -> RawHalfmovePart:
        return RawHalfmovePart(splited[4])

    @classmethod
    def from_FEN(cls, fen: str) -> RawHalfmovePart:
        return RawHalfmovePart.from_SplitedFEN(SplitedFEN.from_FEN(fen))


class HalfmovePart(int):
    @classmethod
    def from_raw(cls, raw: RawHalfmovePart) -> HalfmovePart:
        return HalfmovePart(int(raw))

    @classmethod
    def from_FEN(cls, fen: str) -> HalfmovePart:
        return HalfmovePart.from_raw(RawHalfmovePart.from_FEN(fen))


class RawFullmovePart(str):
    @classmethod
    def from_SplitedFEN(cls, splited: SplitedFEN) -> RawFullmovePart:
        return RawFullmovePart(splited[5])

    @classmethod
    def from_FEN(cls, fen: str) -> RawFullmovePart:
        return RawFullmovePart.from_SplitedFEN(SplitedFEN.from_FEN(fen))


class FullmovePart(int):
    @classmethod
    def from_raw(cls, raw: RawFullmovePart) -> FullmovePart:
        return FullmovePart(int(raw))

    @classmethod
    def from_FEN(cls, fen: str) -> FullmovePart:
        return FullmovePart.from_raw(RawFullmovePart.from_FEN(fen))


class ReplacableSplitedFEN(SplitedFEN):
    @classmethod
    def from_FEN(cls, fen: str) -> ReplacableSplitedFEN:
        return ReplacableSplitedFEN(SplitedFEN.from_FEN(fen))

    def replace_castling(self, castling: CastlingPart) -> ReplacableSplitedFEN:
        return ReplacableSplitedFEN(
            SplitedFEN(FromBoardToColorParts.from_SplitedFEN(self))
            + SplitedFEN([castling])
            + SplitedFEN(FromEnpassantToFullmoveParts.from_SplitedFEN(self))
        )

    def replace_fullmove(self, fullmove: FullmovePart) -> ReplacableSplitedFEN:
        return ReplacableSplitedFEN(
            SplitedFEN(FromBoardToHalfmoveParts.from_SplitedFEN(self)) + SplitedFEN([str(fullmove)])
        )

    def replace_board_color_castling(
        self, board: str, color: ColorPart, castling: CastlingPart
    ) -> ReplacableSplitedFEN:
        return ReplacableSplitedFEN(
            SplitedFEN([board, color, castling]) + SplitedFEN(FromEnpassantToFullmoveParts.from_SplitedFEN(self))
        )
