# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

from infra.rawlegalmoves import RawLegalMoves, RawMove

from .basictype import FEN, SAN
from .microfen import MirroredMicroFEN
from .microsan import MicroSAN
from .validmicrosan import ValidMicroSAN


class CorrectedRawLegalMoves(list[str]):
    @classmethod
    def from_normal_FEN(cls, fen: FEN) -> CorrectedRawLegalMoves:
        return CorrectedRawLegalMoves(RawLegalMoves.from_FEN(fen))

    @classmethod
    def from_mirrored_FEN(cls, fen: FEN) -> CorrectedRawLegalMoves:
        return CorrectedRawLegalMoves([RawMove.castling()] if RawLegalMoves.from_FEN(fen).castlable() else [])

    @classmethod
    def from_FEN(cls, fen: FEN) -> CorrectedRawLegalMoves:
        if fen.split(" ")[1] == "w":
            return CorrectedRawLegalMoves(
                CorrectedRawLegalMoves.from_normal_FEN(fen)
                + CorrectedRawLegalMoves.from_mirrored_FEN(MirroredMicroFEN(fen).value())
            )
        else:
            return CorrectedRawLegalMoves.from_normal_FEN(fen)


class LegalMicroSAN(SAN):
    def legal(self) -> bool:
        try:
            return ValidMicroSAN.from_MicroSAN(MicroSAN(0, [self])).san() != SAN.black_double_move()
        except RuntimeError:
            return False


class LegalSANs(list[SAN]):
    @classmethod
    def from_filtered_legal_moves(cls, legal_moves: filter[str]) -> LegalSANs:
        return LegalSANs(sorted(map(lambda x: SAN(x), legal_moves)))

    @classmethod
    def from_corrected_raw_legal_moves(cls, legal_moves: CorrectedRawLegalMoves) -> LegalSANs:
        return LegalSANs.from_filtered_legal_moves(filter(lambda x: LegalMicroSAN(x).legal(), legal_moves))

    @classmethod
    def from_FEN(cls, fen: FEN) -> LegalSANs:
        return LegalSANs.from_corrected_raw_legal_moves(CorrectedRawLegalMoves.from_FEN(fen))

    @classmethod
    def initial(cls) -> LegalSANs:
        return LegalSANs(
            [
                SAN("e4e5"),
                SAN("e4e6"),
                SAN("e4e7"),
                SAN("f4e5"),
                SAN("f4g5"),
                SAN("f4h6"),
                SAN("g4e5"),
                SAN("g4f6"),
                SAN("g4h6"),
                SAN("h4g5"),
                SAN("h5h6"),
            ]
        )

    @classmethod
    def black_castable(cls) -> LegalSANs:
        return LegalSANs(
            [
                SAN("O-O"),
                SAN("e7e6"),
                SAN("e8f7"),
                SAN("e8f8"),
                SAN("h8f8"),
                SAN("h8g8"),
                SAN("h8h5"),
                SAN("h8h6"),
                SAN("h8h7"),
            ]
        )

    @classmethod
    def white_castable(cls) -> LegalSANs:
        return LegalSANs(
            [
                SAN("O-O"),
                SAN("e4e5"),
                SAN("e4e6"),
                SAN("e4e7"),
                SAN("e4f4"),
                SAN("e4g4"),
                SAN("h4g4"),
                SAN("h4g5"),
                SAN("h5h6"),
            ]
        )
