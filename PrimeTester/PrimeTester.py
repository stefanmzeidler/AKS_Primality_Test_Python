import math


class PrimeTester:

    @staticmethod
    def perfectPower(n):
        b = 2
        while b <= math.log2(n):
            a = math.pow(n, (1 / b))
            if a % 1 == 0:
                return True
            b += 1
        return False
