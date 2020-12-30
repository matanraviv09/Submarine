from battle_ship import *
from battle_ship.battle_ship_client import BattleShipServer, BattleShipClient, ShipMap


def main():
    cl = BattleShipClient('127.0.0.1', 8000)

    print(cl.ship_board)


if __name__ == '__main__':
    main()
