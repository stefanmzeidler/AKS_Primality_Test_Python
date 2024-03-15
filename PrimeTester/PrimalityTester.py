import mpmath as mp


class PrimalityTester:
    """ Test an integer n for primality
        n must be an integer.
    """

    def __init__(self, n):
        """Construct a new PrimalityTester for an integer n
        n must be an integer"""

        if not mp.isint(mp.mpf(n)):
            raise TypeError("Number is not an integer")
        self.__n = mp.mpf(n)
        self.spy = self.SpyClass()

    def perfect_power(self):
        """ Checks whether n is a perfect power
        Returns True if n is a perfect power
         """
        b = mp.mpf(2.0)
        while b <= mp.log(self.__n, 2):
            a = mp.power(self.__n, (1.0 / b))
            if mp.almosteq(a, mp.nint(a)):
                return True
            b += 1
        return False

    def gcd(self, a, b):
        temp = b
        b = mp.fmod(b, a)
        a = temp
        if b != 0:
            a = self.__gcd(a, b)
        return a

    class SpyClass:
        def gcd(self, a, b):
            return _PrimalityTester.__gcd(self, a, b)
