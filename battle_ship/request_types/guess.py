"""
29/12/2020
"""
from battle_ship.consts import MAGIC, RequestsTypes, MAX_GAME_SIZE, HEADER_LENGTH
from battle_ship.base_request import BaseRequest
from battle_ship.request_exceptions import IllegalCoordinateError


class Guess(BaseRequest):
    REQUEST_TYPE = RequestsTypes.GUESS

    def __init__(self, x: int, y: int):
        """
        create a game_request class
        :param x: x coordinates to attack
        :param y: y coordinates to attack
        """
        if not (0 <= x < MAX_GAME_SIZE):
            raise IllegalCoordinateError

        if not (0 <= y < MAX_GAME_SIZE):
            raise IllegalCoordinateError

        self.x = x
        self.y = y
        self.coordinates = chr(y * 0x10 + x).encode()

    def pack(self):
        """
        pack a request
        :return:
        """
        return MAGIC + bytes(self.REQUEST_TYPE) + self.coordinates

    @classmethod
    def load(cls, data: bytes):
        """
        load a packed packet
        :return:
        """
        cls.validate_header(data)
        coordinates_byte = data[HEADER_LENGTH]
        high = coordinates_byte // 0x10
        low = coordinates_byte % 0x10
        return cls(low, high)
