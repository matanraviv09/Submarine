"""
29/12/2020
"""
from battle_ship.consts import MAGIC, RequestsTypes
from battle_ship.base_request import BaseRequest


class GameRequest(BaseRequest):
    REQUEST_TYPE = RequestsTypes.GAMEREQUEST

    def __init__(self):
        """
        create a game_request class
        """
        pass

    def pack(self):
        """
        pack a request
        :return:
        """
        return MAGIC + bytes(self.REQUEST_TYPE)

    @staticmethod
    def load(data: bytes) -> BaseRequest:
        """
        load a packed packet
        :return:
        """
        GameRequest.validate_header(data)
        return GameRequest()
