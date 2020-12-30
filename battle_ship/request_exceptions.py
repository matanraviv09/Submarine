"""
29/12/2020
"""


class WrongMagicError(Exception):
    """
    Raise when there is a wrong magic number at the beginning of package
    """

    def __str__(self):
        return "Wrong magic number in the beginning of package"


class WrongRequestTypeError(Exception):
    """
    Raise when the RequestType does not match
    """

    def __str__(self):
        return "Wrong Request Type"


class IllegalCoordinateError(Exception):
    """
    Raise when Coordinate are Illegal
    """

    def __str__(self):
        return "Wrong Request Type"


class WrongPacketSyntaxError(Exception):
    """
    Raise when the packet is not built correctly
    """

    def __str__(self):
        return "packet was not built correctly"


class NoShipSizeError(WrongPacketSyntaxError):
    """
    Raise when no ship size is given inside the result packet
    """

    def __str__(self):
        return "No Ship Size"
