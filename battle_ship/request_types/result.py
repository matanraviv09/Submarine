"""
29/12/2020
"""
from battle_ship.consts import MAGIC, RequestsTypes, HEADER_LENGTH
from battle_ship.base_request import BaseRequest
from battle_ship.request_exceptions import NoShipSizeError

SINK_REQUEST_CODE = 3


class Result(BaseRequest):
    REQUEST_TYPE = RequestsTypes.GUESS

    def __init__(self, result_code: int, sub_length: int = None):
        """
        create a game_request class
        :param result_code: result code of result
        :param sub_length: optional - length of sub
        """
        self.result_code = result_code
        self.sub_length = sub_length

        self.result_code_bytes = chr(result_code).encode('utf-8')
        if sub_length:
            self.sub_length_bytes = chr(sub_length).encode('utf-8')
        else:
            self.sub_length_bytes = bytes(0)

    def pack(self):
        """
        pack a request
        :return:
        """
        return MAGIC + bytes(self.REQUEST_TYPE) + self.result_code_bytes + self.sub_length_bytes

    @classmethod
    def load(cls, data: bytes) -> BaseRequest:
        """
        load a packed packet
        :return:
        """
        cls.validate_header(data)
        result_code = data[HEADER_LENGTH]
        sub_length = None
        if result_code == SINK_REQUEST_CODE:
            try:
                sub_length = data[HEADER_LENGTH + 1]
            except IndexError as e:
                raise NoShipSizeError from e
        return cls(result_code, sub_length)
