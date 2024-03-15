import unittest

import sympy
from PrimeTester import PrimalityTester
import math
import mpmath


class MyTestCase(unittest.TestCase):
    def test_perfect_power(self):
        tester = PrimalityTester.PrimalityTester(100)
        assertTrue(tester.__perfectPower)




if __name__ == '__main__':
    unittest.main()
