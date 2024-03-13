import math
import mpmath


class PrimeTester:

    @staticmethod
    def perfectPower(p):
        # print('Testing the number: ' + str(p))
        c = 2.0
        b = mpmath.mpf(2.0)
        while b <= mpmath.log(p, 2):
            # print('b is currently ' + str(b))
            a = mpmath.power(p, (1.0 / b))
            # print('a is currently ' + str(a))
            if mpmath.almosteq(a, mpmath.nint(a)):
                return True
            b += 1
        return False

# n = 2
# while n < 1000:
#     if not PrimeTester.perfectPower(math.pow(n, n)):
#         print("The value " + str(n) + " failed when it shouldn't have.")
#         break
#     n += 1
