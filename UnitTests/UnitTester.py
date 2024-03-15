import unittest
import sympy
from PrimeTester import PrimalityTester
import math
import mpmath as mp


class MyTestCase(unittest.TestCase):
    def test_perfect_power(self):
        n = mp.mpf(2.0)
        count = 1
        while count < 100:
            tester = PrimalityTester.PrimalityTester(n)
            self.assertTrue(tester.perfect_power())
            n = mp.power(n, n)
            count += 1





if __name__ == '__main__':
    unittest.main()
