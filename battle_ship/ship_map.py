"""
30/12/2020
"""
from .ship import Ship


class ShipPlacementError(Exception):
    pass


SUB_LENGTHS = [2, 3, 3, 4, 5]


class ShipMap:

    def __init__(self, size):
        """

        :param size: size of all the borders of a square map
        """
        self.size = size
        self.ships = []
        self.git_hit = []

    def add_ship(self, ship_to_add: Ship):
        """
        adds a ship
        :param ship_to_add:
        :return:
        """
        # to get the axis of the ship
        for location in ship_to_add.get_ship_vector():
            if not self.check_location(location):
                raise ShipPlacementError

        self.ships.append(ship_to_add)

    def check_ships(self):
        """

        :return: True if a ship was sunk
        """
        to_remove = []
        did_remove = False
        for ship_index in range(len(self.ships)):
            if all([loc in self.git_hit for loc in self.ships[ship_index].get_ship_vector()]):
                to_remove.append(ship_index)

        for ship in to_remove:
            del self.ships[ship]
            did_remove = True

        return did_remove

    def check_location(self, location) -> bool:
        """

        :param location: location to check
        :return:
        """
        if not all([0 <= axis_value < self.size for axis_value in location]):
            return False
        for ship in self.ships:
            if location in ship.get_ship_vector():
                return False
        return True

    def get_attacked(self, loc_x, loc_y):
        self.git_hit.append((loc_x, loc_y))
        return self.check_ships()

    def __str__(self):
        """

        :return:
        """
        all_points = []
        for ship in self.ships:
            all_points += ship.get_ship_vector()

        all_lines = []
        for y in range(self.size):
            curr_line = []
            for x in range(self.size):
                pos = (x, y)
                pos_hit = pos in self.git_hit
                pos_is_ship = pos in all_points
                if pos_hit and pos_is_ship:
                    curr_line.append('SS')
                elif pos_hit:
                    curr_line.append('//')
                elif pos_is_ship:
                    curr_line.append('##')
                else:
                    curr_line.append('~~')
            all_lines.append("".join(['|'] + curr_line + ['|']))
        return "\n".join(all_lines)

    def is_alive(self):
        return len(self.ships) > 0

    def initialize_board(self):
        """

        """
        print("Now initializing board")
        for length in SUB_LENGTHS:
            print(self.ship_board)

            print(f"ship with length of {length}")
            x = int(input('Enter x position: '))
            y = int(input('Enter y position: '))
            direction = int(input("0:UP\n1:RIGHT\n2:DOWN\n3:LEFT\nEnter index of rotation: "))
            ship = Ship(x, y, length, direction)

            self.ship_board.add_ship(ship)
