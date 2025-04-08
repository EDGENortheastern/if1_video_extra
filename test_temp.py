import unittest
from temp import celsius_to_far

class TestTemp(unittest.TestCase):
    def test_tests_work(self):
        self.assertEqual(2+2,4)

    def test_celsius_to_far_happy(self):
        self.assertEqual(celsius_to_far(0), 32)

if __name__ == "__main__":
    unittest.main()