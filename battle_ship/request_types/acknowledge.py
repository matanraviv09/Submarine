"""
29/12/2020
"""
from battle_ship.consts import MAGIC, RequestsTypes, HEADER_LENGTH
from battle_ship.base_request import BaseRequest
from .result import Result


class Acknowledge(BaseRequest):
    REQUEST_TYPE = RequestsTypes.ACKNOWLEDGE

    def __init__(self, result_code: int):
        """
        create a game_request class
        :param result_code: result code of result
        """
        self.result_code = result_code
        self.result_code_bytes = chr(result_code).encode('utf-8')

    def pack(self):
        """
        pack a request
        :return:
        """
        return MAGIC + bytes(self.REQUEST_TYPE) + self.result_code_bytes

    @classmethod
    def load(cls, data: bytes):
        """
        load a packed packet
        :return:
        """
        cls.validate_header(data)
        result_code = data[HEADER_LENGTH]
        return cls(result_code)

    @classmethod
    def load_from_result(cls, result_packet: Result):
        """

        :param result_packet:
        :return:
        """
        result_code = result_packet.result_code
        return cls(result_code)
