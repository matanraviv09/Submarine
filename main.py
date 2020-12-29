from battle_ship import *
from battle_ship.request_types.result import *

print(Result.load(Result(3).pack()).pack())
