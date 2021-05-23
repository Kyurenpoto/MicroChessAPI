# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from domain.implementation.microfen import MicroFEN

from .basictype import FEN
from .mirroredrow import MirroredRow
from .splitablefen import BoardPart


class PureBoardPart(str):
    @classmethod
    def from_board_part(cls, board: BoardPart) -> PureBoardPart:
        return PureBoardPart(board.board)


class PieceMirroredBoardPart(PureBoardPart):
    @classmethod
    def from_pure_board_part(cls, pure: PureBoardPart) -> PieceMirroredBoardPart:
        return PieceMirroredBoardPart("".join(map(lambda x: PieceMirroredBoardPart.mirror_piece(x), pure)))

    @classmethod
    def mirror_piece(cls, piece: str) -> str:
        if piece.isupper():
            return piece.lower()
        if piece.islower():
            return piece.upper()
        return piece


class SplitedBoardPart(list[str]):
    @classmethod
    def from_pure_board_part(cls, pure: PureBoardPart) -> SplitedBoardPart:
        return SplitedBoardPart(pure.split("/"))

    def join_parts(self) -> str:
        return "/".join(self)


class MirroredSplitedBoardPart(SplitedBoardPart):
    @classmethod
    def from_splited_board_part(cls, splited: SplitedBoardPart) -> MirroredSplitedBoardPart:
        return MirroredSplitedBoardPart([MirroredRow(row).value() for row in splited[4::-1]] + splited[5:])


class MirroredBoardPart(str):
    @classmethod
    def from_piece_mirrored_board_part(cls, mirrored: PieceMirroredBoardPart) -> MirroredBoardPart:
        return MirroredBoardPart(
            MirroredSplitedBoardPart.from_splited_board_part(
                SplitedBoardPart.from_pure_board_part(mirrored)
            ).join_parts()
        )

    @classmethod
    def from_board_part(cls, board: BoardPart) -> MirroredBoardPart:
        return MirroredBoardPart.from_piece_mirrored_board_part(
            PieceMirroredBoardPart.from_pure_board_part(PureBoardPart.from_board_part(board))
        )

    @classmethod
    def from_FEN(cls, fen: FEN) -> MirroredBoardPart:
        return MirroredBoardPart.from_board_part(BoardPart.from_MicroFEN(MicroFEN.from_index_with_FENS(0, [fen])))
