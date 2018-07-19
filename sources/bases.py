import unittest

# this module manages the value's base of each player. The main key is the 
# player_id.

class Bases:

    def __init__(self):
        self._base_list = []

class TestBases(unittest.TestCase):
    def test_init(self):
        bases = Bases()

if __name__ == "__main__":
    unittest.main()