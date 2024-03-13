import unittest
from PrimeTester import PrimeTester
import math
import mpmath


class MyTestCase(unittest.TestCase):
    # def test_perfectPower_small(self):
    #     self.assertTrue(PrimeTester.PrimeTester.perfectPower(8))
    #     self.assertTrue(PrimeTester.PrimeTester.perfectPower(3125))
    #     self.assertFalse(PrimeTester.PrimeTester.perfectPower(7))
    #     self.assertTrue(PrimeTester.PrimeTester.perfectPower(343))
    #     self.assertTrue(PrimeTester.PrimeTester.perfectPower(823543))
    #
    # def test_perfectPower_large(self):
    #     self.assertTrue(PrimeTester.PrimeTester.perfectPower(math.pow(25, 25)))
    #     self.assertFalse(PrimeTester.PrimeTester.perfectPower(math.pow(25, 25)) - 1)
    #     self.assertTrue(PrimeTester.PrimeTester.perfectPower(math.pow(100, 100)))
    #     self.assertFalse(PrimeTester.PrimeTester.perfectPower(mpmath.power(1001, 1001))-1)
    #
    # def test_perfectPower_loop(self):
    #     n = 2
    #
    #     while n < 100:
    #         print('Testing the number: ' + str(n))
    #         self.assertTrue(PrimeTester.PrimeTester.perfectPower(mpmath.power(n, n)), "The value " + str(n) + " failed")
    #         n += 1

    # def test_mpmath(self):
    #     self.assertEqual(mpmath.mpf(1.0),1)

    def test_smallestr(self):
        self.assertFalse(PrimeTester.PrimeTester.smallest_r(31))
        self.assertFalse(PrimeTester.PrimeTester.smallest_r(37))




if __name__ == '__main__':
    unittest.main()
