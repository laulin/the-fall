import unittest
from collections import namedtuple
from itertools import cycle

# this module manages the value's base of each player. The main key is the 
# player_id.

Base = namedtuple("Base", [ "level_trade_post", 
                            "level_weapon_factory", 
                            "level_vehicule_warhouse", 
                            "level_barack"])

class Bases:

    def __init__(self):
        self._base_dict = dict()
        self._INIT_BASE_VALUES = (0,)*4

    def create(self, player_id):
        # this function creates a base

        # check if the player doesn't already exist
        if player_id in self._base_dict:
            raise Exception("Player {} already has a base".format(player_id))

        base = Base(*self._INIT_BASE_VALUES)
        self._base_dict[player_id] = base

class TestBases(unittest.TestCase):
    def test_init(self):
        bases = Bases()

    def test_create_base(self):
        bases = Bases()
        player_id = 10
        bases.create(player_id)

    def test_create_base_player_already_exists(self):
        bases = Bases()
        player_id = 10
        bases.create(player_id)
        # error !
        with self.assertRaises(Exception):
            bases.create(player_id)


if __name__ == "__main__":
    unittest.main()