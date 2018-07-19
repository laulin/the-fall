import unittest
from collections import namedtuple

PlayerAttribute = namedtuple("PlayerAttribute", ["playerid","email", "password", "nickname"])

class Players:
    def __init__(self):
        self._players_list = []
        self._last_player_id = 0
    def create(self, email, password, nickname):
        playerid = self._last_player_id
        self._last_player_id += 1
        player = PlayerAttribute(playerid,email, password, nickname)
        self._players_list.append(player)


class TestClass(unittest.TestCase):
    def test_Players_Constructor(self):
        player = Players()
    def test_CreatePlayer(self):
        player = Players()
        player.create("test@test.com","azerty","test")

if __name__ == "__main__":
    unittest.main()