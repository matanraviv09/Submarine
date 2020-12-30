"""
30/12/2020
"""
import socket
import battle_ship
from battle_ship.ship_map import ShipMap, Ship
from battle_ship.request_exceptions import IllegalCoordinateError, WrongPacketSyntaxError

SIZE_OF_WORLD = 10

MSG_LIST = [
    "MISS",
    "HIT",
    "HIT AND SUNK",
    "HIS AND SUNK ALL"
]


def get_location_input():
    """

    :return:
    """
    x = int(input("Enter x location to attack:"))
    y = int(input("Enter y location to attack:"))
    return x, y


def play_turn(sock: socket.socket):
    """

    :return:
    """
    result = 1
    while result in [1, 2]:
        x, y = get_location_input()
        sock.send(battle_ship.Guess(x, y).pack())
        result_struct = battle_ship.Result.load(sock.recv(1024))
        result, sub_length = result_struct.result_code, result_struct.sub_length
        sock.send(battle_ship.Acknowledge.load_from_result(result_struct))

        print(MSG_LIST[result])
        return result


def calculate_result_code(did_hit, did_sink, is_alive):
    if not did_hit:
        return 0
    elif did_hit and did_sink and is_alive:
        return 2
    elif did_hit and did_sink and not is_alive:
        return 3
    return 1


def recv_with_error_handle(sock: socket.socket):
    """

    :param sock:
    :return:
    """
    recv_msg = sock.recv(1024)
    if isinstance(battle_ship.load_request(recv_msg), battle_ship.Error):
        sock.send(battle_ship.Acknowledge(6).pack())
        return None
    else:
        return recv_msg


class BattleShipClient:

    def __init__(self, port, address, size_of_world=SIZE_OF_WORLD):
        """

        :param size_of_world: size of world
        """
        self.ships = []

        self.ship_board = ShipMap(size_of_world)

        self.port = port
        self.address = address

        self.did_win = False

        self.socket = socket.socket()
        self.init_game()

    def init_game(self):
        """

        :return:
        """
        self.socket.connect((self.address, self.port))
        self.socket.send(battle_ship.GameRequest().pack())
        response = recv_with_error_handle(self.socket)
        if not response or not battle_ship.GameReply.load(response).response:
            return
        self.ship_board.initialize_board()
        self.socket.send(battle_ship.Order().pack())
        battle_ship.Order.load(recv_with_error_handle(self.socket))
        self.play_game()

    def play_game(self):
        """

        :return:
        """
        while self.ship_board.is_alive() and not self.did_win:
            self.did_win = 3 == play_turn(self.socket)
            self.get_attacked()

        if not self.ship_board.is_alive():
            print('you lose')
        elif self.did_win:
            print('you win')

    def get_attacked(self):
        """

        :return:
        """
        result_code = 1
        while result_code in [1, 2]:
            guess_struct = battle_ship.Guess.load(recv_with_error_handle(self.socket))
            try:
                did_hit = self.ship_board.check_location((guess_struct.x, guess_struct.y))
                did_sink = self.ship_board.get_attacked(guess_struct.x, guess_struct.y)
            except IllegalCoordinateError:
                self.socket.send(battle_ship.Error(2).pack())
                continue
            result_code = calculate_result_code(did_hit, did_sink, self.ship_board.is_alive())
            self.socket.send(battle_ship.Result(result_code).pack())
            recv_msg = recv_with_error_handle(self.socket)
            if not recv_msg or result_code != battle_ship.Acknowledge.load(recv_msg).result_code:
                raise WrongPacketSyntaxError


class BattleShipServer:

    def __init__(self, port, size_of_world=SIZE_OF_WORLD):
        """

        :param size_of_world: size of world
        """
        self.ships = []

        self.ship_board = ShipMap(size_of_world)

        self.port = port

        self.did_win = False

        self.server_socket = socket.socket()
        self.socket = None
        self.init_game()

    def init_game(self):
        """

        :return:
        """
        self.server_socket.bind(('0.0.0.0', self.port))
        self.server_socket.listen(1)
        self.socket, _ = self.server_socket.accept()

      """
      finish server flow
      """
