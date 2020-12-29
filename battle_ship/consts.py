""""
29/12/2020
"""
from enum import Enum

MAGIC = b"BS1p"
MAGIC_LENGTH = len(MAGIC)

GAME_TYPE_INDEX = 4

HEADER_LENGTH = 5

MAX_GAME_SIZE = 0xf


class RequestsTypes(Enum):
    GAMEREQUEST = 0
    GAMEREPLY = 1
    ORDER = 2
    GUESS = 3
    RESULT = 4
    ACKNOWLEDGE = 5
    ERROR = 6

    def __iadd__(self, other):
        print('kak')
        return other + bytes(self)

    def __bytes__(self):
        """
        override the bites operator
        :return:
        """
        return chr(self.value).encode('utf-8')
