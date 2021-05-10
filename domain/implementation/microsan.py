# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: GPL-3.0-only

from typing import Final, NewType, Optional, Set

SAN = NewType("SAN", str)

MICRO_CASTLING_SAN: Final[SAN] = SAN("O-O")
MICRO_FIRST_MOVE_SAN: Final[SAN] = SAN("h5h6")
MICRO_SECOND_MOVE_SAN: Final[SAN] = SAN("e7e6")
MICRO_KING_SIDE_MOVE_SAN: Final[SAN] = SAN("h4g4")
MICRO_BLACK_DOUBLE_MOVE_SAN: Final[SAN] = SAN("e7e5")

PROMOTIONABLE_PIECES: Final[str] = "QqRrBbNn"
MOVABLE_PIECES: Final[str] = "KkQqRrBbNn"
VALID_SQUARES: Final[Set[str]] = set([i + j for j in "45678" for i in "efgh"])


class ValidSquares:
    __slots__ = ["__squares"]

    squares: str

    def __init__(self, squares: str):
        self.__squares = squares

    def value(self) -> Optional[str]:
        return self.__squares if (self.__squares[:2] in VALID_SQUARES and self.__squares[2:] in VALID_SQUARES) else None


class CreatedMicroSAN:
    __slots__ = ["__squares", "__piece", "__promotion"]

    __squares: Optional[str]
    __piece: str
    __promotion: str

    def __init__(self, squares: Optional[str], piece: str, promotion: str):
        self.__squares = squares
        self.__piece = piece
        self.__promotion = promotion

    def value(self) -> Optional[SAN]:
        return None if self.__squares is None else SAN(self.__piece + self.__squares + self.__promotion)


class ValidCastlingSAN:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> Optional[SAN]:
        return self.__san if self.__san == MICRO_CASTLING_SAN else None


class ValidPromotionSAN:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> Optional[SAN]:
        return (
            CreatedMicroSAN(ValidSquares(self.__san[:-1]).value(), "", self.__san[-1]).value()
            if (self.__san[-1] in PROMOTIONABLE_PIECES and len(str(self.__san)) == 5)
            else None
        )


class ValidAdvancedSAN:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> Optional[SAN]:
        return (
            CreatedMicroSAN(ValidSquares(self.__san[1:]).value(), self.__san[0], "").value()
            if (self.__san[0] in MOVABLE_PIECES and len(str(self.__san)) == 5)
            else None
        )


class ValidPawnSAN:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> Optional[SAN]:
        return (
            CreatedMicroSAN(ValidSquares(self.__san[:]).value(), "", "").value() if len(str(self.__san)) == 4 else None
        )


class ValidMicroSAN:
    __slots__ = ["__san"]

    __san: SAN

    def __init__(self, san: SAN):
        self.__san = san

    def value(self) -> Optional[SAN]:
        castling_san = ValidCastlingSAN(self.__san).value()
        if castling_san is not None:
            return castling_san

        promotion_san = ValidPromotionSAN(self.__san).value()
        if promotion_san is not None:
            return promotion_san

        advanced_san = ValidAdvancedSAN(self.__san).value()
        if advanced_san is not None:
            return advanced_san

        pawn_san = ValidPawnSAN(self.__san).value()
        if pawn_san is not None:
            return pawn_san

        return None
