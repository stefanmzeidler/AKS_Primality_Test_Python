import math
import mpmath


class PrimeTester:

    @staticmethod
    def perfectPower(p):
        # print('Testing the number: ' + str(p))
        b = mpmath.mpf(2.0)
        while b <= mpmath.log(p, 2):
            # print('b is currently ' + str(b))
            a = mpmath.power(p, (1.0 / b))
            # print('a is currently ' + str(a))
            if mpmath.almosteq(a, mpmath.nint(a)):
                return True
            b += 1
        return False

    @staticmethod
    def smallest_r(n):
    # returns false if not prime, continue onto next step
        maxk = mpmath.floor(mpmath.power(mpmath.log(n, 2), 2))
        # print(str(maxk))
        term2 = mpmath.log(n, 2)
        term3 = mpmath.power(term2, 5)
        term4 = mpmath.ceil(term3)
        maxr = PrimeTester.mpmax(3, term4)
        # print(str(maxr))
        nextr = True
        r = mpmath.ceil(mpmath.power(term2, 2))
        while nextr:  # and r < maxr
            nextr = False
            if not PrimeTester.gcd(r, n) == 1:
                continue
            k = 1
            while (not nextr) and k <= maxk:

                part1 = mpmath.power(n, k)
                # print("part 1: " + str(part1))
                part2 = mpmath.fmod(part1, r)
                # print("part 2: " + str(part2))
                # print(str(part2 == 1))
                # print(str(part2 == 0))
                if part2 == 1.0 or part2 == 0.0:
                    nextr = True
                k += 1
            r += 1
        r = r - 2
        if n <= r:
            return True
        else:
            return False

    @staticmethod
    def polynomialRemainder(a,b):
        mpmath.poly
    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def mpmax(x, y):
        if mpmath.fsub(x, y) > 0:
            return x
        else:
            return y



print(str(PrimeTester.smallest_r(37)))