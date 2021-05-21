# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, NamedTuple, Optional

from infra.rawlegalmoves import CASTLING_SAN, RawLegalMoves

from .basictype import FEN, SAN
from .microfen import MirroredMicroFEN
from .microsan import MicroSAN
from .validmicrosan import MICRO_BLACK_DOUBLE_MOVE_SAN, ValidMicroSAN


class LegalSAN(NamedTuple):
    san: SAN

    def value(self) -> Optional[SAN]:
        try:
            return ValidMicroSAN(MicroSAN(0, [self.san])).value().san()
        except RuntimeError:
            return None


MICRO_MAX_LEGAL_MOVES: Final[int] = 34
MICRO_INITIAL_LEGAL_MOVES: Final[list[SAN]] = [
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
MICRO_BLACK_CASTLABLE_LEGAL_MOVES: Final[list[SAN]] = [
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
MICRO_WHITE_CASTLABLE_LEGAL_MOVES: Final[list[SAN]] = [
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


class CorrectedRawLegalMoves(NamedTuple):
    fen: FEN

    def value(self) -> list[str]:
        if self.fen.split(" ")[1] == "w":
            return RawLegalMoves(self.fen).value() + (
                [CASTLING_SAN] if CASTLING_SAN in RawLegalMoves(MirroredMicroFEN(self.fen).value()).value() else []
            )
        else:
            return RawLegalMoves(self.fen).value()


class LegalSANs(NamedTuple):
    fen: FEN

    def value(self) -> list[SAN]:
        return sorted(
            filter(
                lambda x: x != MICRO_BLACK_DOUBLE_MOVE_SAN,
                filter(
                    lambda x: LegalSAN(x).value() is not None,
                    map(lambda x: SAN(x), CorrectedRawLegalMoves(self.fen).value()),
                ),
            )
        )
