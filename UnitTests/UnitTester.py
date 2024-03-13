import unittest
from PrimeTester import PrimeTester


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(PrimeTester.PrimeTester.perfectPower(8))


if __name__ == '__main__':
    unittest.main()
