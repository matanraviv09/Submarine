from battle_ship import *
from battle_ship.battle_ship_client import BattleShipClientP2P, ShipMap


def main():
    cl = BattleShipClientP2P('127.0.0.1', 8000)

    print(cl.ship_board)


if __name__ == '__main__':
    main()
