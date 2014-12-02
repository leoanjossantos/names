import unittest
from names import get_name

class NamesTests(unittest.TestCase):
    def test_get_name(self):
        name = get_name()
        self.assertIsNotNone(name)

    def test_get_name_returns_random_name(self):
        name = get_name()
        name2 = get_name()
        self.assertNotEqual(name, name2)

if __name__ == "__main__":
    unittest.main()
