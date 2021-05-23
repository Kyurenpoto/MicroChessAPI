# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from domain.implementation.microfen import MicroFEN

from .basictype import FEN
from .splitablefen import BoardPart


class Piece(str):
    def mirrored(self) -> Piece:
        if self.isupper():
            return Piece(self.lower())
        if self.islower():
            return Piece(self.upper())
        return self


class PureBoardPart(str):
    @classmethod
    def from_FEN(cls, fen: FEN) -> PureBoardPart:
        return PureBoardPart(BoardPart.from_MicroFEN(MicroFEN.from_index_with_FENs(0, [fen])).board)

    def mirrored(self) -> PureBoardPart:
        return PureBoardPart("".join(map(lambda x: Piece(x).mirrored(), self)))


class Row(str):
    def expanded(self) -> Row:
        return Row(self if self[0] == "4" else "4" + str(int(self[0]) - 4) + self[1:])

    def partial_mirrored(self) -> Row:
        return Row(self[0] + self[:0:-1])

    def left_space_squeezed(self) -> Row:
        return Row(str(4 + int(self[1])) + self[2:])

    def squeezed(self) -> Row:
        return self.left_space_squeezed() if self[1] in "123" else self

    def mirrored(self) -> Row:
        return self if self == "8" else Row(self).expanded().partial_mirrored().squeezed()


class SplitedBoardPart(list[str]):
    @classmethod
    def from_pure_board_part(cls, pure: PureBoardPart) -> SplitedBoardPart:
        return SplitedBoardPart(pure.split("/"))

    def joined(self) -> str:
        return "/".join(self)

    def mirrored(self) -> SplitedBoardPart:
        return SplitedBoardPart([str(Row(row).mirrored()) for row in self[4::-1]] + self[5:])


class MirroredBoardPart(str):
    @classmethod
    def from_piece_mirrored_board_part(cls, piece_mirrored: PureBoardPart) -> MirroredBoardPart:
        return MirroredBoardPart(SplitedBoardPart.from_pure_board_part(piece_mirrored).mirrored().joined())

    @classmethod
    def from_FEN(cls, fen: FEN) -> MirroredBoardPart:
        return MirroredBoardPart.from_piece_mirrored_board_part(PureBoardPart.from_FEN(fen).mirrored())
