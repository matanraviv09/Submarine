"""
29/12/2020
"""
from battle_ship.consts import MAGIC, RequestsTypes
from battle_ship.base_request import BaseRequest


class Order(BaseRequest):
    REQUEST_TYPE = RequestsTypes.ORDER

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
    def load(data: bytes):
        """
        load a packed packet
        :return:
        """
        Order.validate_header(data)
        return Order()
