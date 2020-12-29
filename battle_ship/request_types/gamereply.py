"""
29/12/2020
"""
from battle_ship.consts import MAGIC, RequestsTypes, HEADER_LENGTH
from battle_ship.base_request import BaseRequest


class GameReply(BaseRequest):
    REQUEST_TYPE = RequestsTypes.GAMEREPLY

    def __init__(self, response: bool):
        """
        create a game_request class
        :param response: boolean for a response request
        """
        self.response = chr(response).encode('utf-8')

    def pack(self):
        """
        pack a request
        :return:
        """
        return MAGIC + bytes(self.REQUEST_TYPE) + self.response

    @staticmethod
    def load(data: bytes) -> BaseRequest:
        """
        load a packed packet
        :return:
        """
        GameReply.validate_header(data)
        response_byte = data[HEADER_LENGTH]
        response = bool(response_byte)
        return GameReply(response)
