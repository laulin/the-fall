import unittest
from collections import namedtuple
from itertools import cycle

# this module manages the value's base of each player. The main key is the 
# player_id.

Base = namedtuple("Base", [ "level_trading_post", 
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

    def get_level(self, player_id, building):
        # this function is used to get level of one building
        base = self._base_dict[player_id]
        field = "level_{}".format(building)

        if field not in base._fields:
            raise Exception("building {} doesn't exists".format(building))

        return base._asdict()[field]

    def inc_level(self, player_id, building):
        # this function inc the building level
        base = self._base_dict[player_id]
        field = "level_{}".format(building)

        if field not in base._fields:
            raise Exception("building {} doesn't exists".format(building))

        value = base._asdict()[field]
        new_base = base._replace(**{field : value +1})
        self._base_dict[player_id] = new_base

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

    def test_get_level(self):
        bases = Bases()
        player_id = 10
        bases.create(player_id)

        result = bases.get_level(player_id, "trading_post")

        self.assertEqual(result, 0)

    def test_get_level_no_player(self):
        bases = Bases()
        player_id = 10
        bases.create(player_id)

        with self.assertRaises(Exception):
            bases.get_level(player_id-1, "trading_post")

    def test_inc_level(self):
        bases = Bases()
        player_id = 10
        bases.create(player_id)

        bases.inc_level(player_id, "trading_post")
        result = bases.get_level(player_id, "trading_post")

        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()