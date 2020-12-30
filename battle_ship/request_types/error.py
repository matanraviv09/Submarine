"""
29/12/2020
"""
from battle_ship.consts import MAGIC, RequestsTypes, HEADER_LENGTH
from battle_ship.base_request import BaseRequest
from battle_ship.request_exceptions import WrongPacketSyntaxError


class Error(BaseRequest):
    REQUEST_TYPE = RequestsTypes.ERROR

    def __init__(self, error_code: int):
        """
        create a game_request class
        :param error_code: result code of result
        """
        self.error_code = error_code
        self.error_code_bytes = chr(error_code).encode('utf-8')

    def pack(self):
        """
        pack a request
        :return:
        """
        return MAGIC + bytes(self.REQUEST_TYPE) + self.error_code_bytes

    @classmethod
    def load(cls, data: bytes):
        """
        load a packed packet
        :return:
        """
        cls.validate_header(data)
        try:
            result_code = data[HEADER_LENGTH]
        except IndexError as e:
            raise WrongPacketSyntaxError from e
        return cls(result_code)
