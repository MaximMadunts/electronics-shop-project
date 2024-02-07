import unittest
from src.keyboard import Keyboard


class TestKeyboard(unittest.TestCase):
    def test_keyboard_creation(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert str(kb) == "Dark Project KD87A"


if __name__ == '__main__':
    unittest.main()
