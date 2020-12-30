"""
30/12/2020
"""
#             0:UP    1:RIGHT  2:DOWN  3:LEFT
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Ship:

    def __init__(self, x: int, y: int, length: int, direction: int):
        """

        :param x: x position
        :param y: y position
        :param direction: direction of ship
        :param length: length of ship
        """
        self.location = x, y
        self.length = length
        self.direction = direction

    def get_ship_vector(self):
        """

        :return: an array of all the spots a ship is taking
        """
        ship_vector = []
        for i in range(self.length):
            ship_vector.append((self.location[0] + DIRECTIONS[self.direction][0] * i,
                                self.location[1] + DIRECTIONS[self.direction][1] * i))

        return ship_vector
