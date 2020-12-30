"""
29/12/2020
"""
from abc import ABC, abstractmethod

from battle_ship.request_exceptions import WrongRequestTypeError, WrongMagicError
from battle_ship.consts import GAME_TYPE_INDEX, MAGIC, MAGIC_LENGTH


def validate_request_type(request_type_class, request_id: bytes):
    """

    :param request_type_class:
    :param request_id: request id to validate
    :raise: WrongRequestTypeError when not valid
    """
    if request_id != request_type_class.REQUEST_TYPE.value:
        raise WrongRequestTypeError


def validate_magic(magic_sequence: bytes):
    """

    :param magic_sequence:
    :return:
    """
    if magic_sequence != MAGIC:
        raise WrongMagicError


def load_request(data: bytes):
    """

    :param data: data of packet
    :return:
    """
    request_id = data[MAGIC_LENGTH]
    request_class = BaseRequest.all_request_type_classes[request_id]
    return request_class.load(data)


class BaseRequest(ABC):
    REQUEST_TYPE = None
    all_request_type_classes = {}

    def __init_subclass__(cls, **kwargs):
        """

        :param kwargs:
        :return:
        """
        BaseRequest.all_request_type_classes[cls.REQUEST_TYPE.value] = cls

    @abstractmethod
    def pack(self):
        """
        pack a request
        :return:
        """
        pass

    @staticmethod
    @abstractmethod
    def load(data: bytes):
        """
        load a packed packet
        :return:
        """
        pass

    @classmethod
    def validate_header(cls, data: bytes):
        validate_request_type(cls, data[GAME_TYPE_INDEX])
        validate_magic(data[:MAGIC_LENGTH])
