import math
import mpmath
import numpy
import sympy as sp
from sympy import Poly, symbols, binomial, div
from sympy.abc import x


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
        #r = mpmath.ceil(mpmath.power(term2, 2))
        rsmall = 2
        while nextr:  # and r < maxr
            nextr = False
            # if not PrimeTester.gcd(rsmall, n) == 1:
            #     continue
            k = 1
            while (not nextr) and k <= maxk:
                part1 = mpmath.power(n, k)
                print("part1: " + str(part1))
                part2 = mpmath.fmod(part1, rsmall)
                print("part2: " + str(part2))
                if part2 == 1.0 or part2 == 0.0:
                    nextr = True
                k += 1
            rsmall += 1
            print("r is now: " + str(rsmall))
        rsmall = rsmall - 2
        return rsmall

    @staticmethod
    def polynomialRemainderTest(r, n2):
        euphi_rt = mpmath.sqrt(sp.totient(r))
        intermed = mpmath.log(n2, 2)
        max = mpmath.floor(euphi_rt * intermed)

        a = 1
        count = 1
        while (a <= max):
            print("loop: " + str(count))
            count += 1
            expression1 = Poly(PrimeTester.polyremainder1(n2, a))
            print("Polyremainder1:  " + str(expression1.as_expr()))
            expression2 = Poly(PrimeTester.polyremainder2(r))
            print(expression2.as_expr())
            _, remainder = div(expression1.as_expr(), expression2.as_expr())
            print(remainder)
            # polynomial_modulo = Poly(PrimeTester.polymodterm1(n2, a) - remainder, x).as_expr() % x
            polymodterm = PrimeTester.polymodterm1(n2, a)
            print("Polymodterm: " + str(polymodterm))
            result = PrimeTester.polynomial_mod(polymodterm - remainder, n2)
            print(result)
            if result != 0:
                return False
        return True

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

    @staticmethod
    def PolyModulo(f, n, x, r):
        xr_minus_1 = numpy.power(x, r) - 1
        remainder = sp.rem(f, xr_minus_1, x)
        return sp.rem(remainder, n, x)

    @staticmethod
    def getExpression1(exp, a):
        # x, a = symbols('x a')
        x = symbols('x')
        # Define the exponent and the expression
        exponent = exp
        expression = (x + a) ** exponent

        # Initialize an empty expression for the expanded form
        expanded_form = 0

        # Iterate over the terms in the expansion
        for k in range(exponent + 1):
            coefficient = binomial(exponent, k)  # Compute the binomial coefficient
            term = coefficient * (a ** (exponent - k)) * (x ** k)  # Compute the term
            expanded_form += term  # Add the term to the expanded form

        return expanded_form
        # Print the expanded form

    @staticmethod
    def polymodterm1(n, a):
        # Define the symbol
        x = symbols('x')
        # a = symbols('a')
        # Initialize an empty expression for the expanded form
        expanded_form = 0

        # Iterate over the terms in the expansion
        for k in range(n + 1):
            coefficient = binomial(n, k)  # Compute the binomial coefficient
            term = coefficient * x ** (n - k) * a ** k  # Compute the term
            expanded_form += term  # Add the term to the expanded form

        return expanded_form

    @staticmethod
    def polyremainder2(r):
        # Define the symbol
        x = symbols('x')

        # Initialize an empty expression for the expanded form
        expanded_form = 0

        # Iterate over the terms in the expansion
        for k in range(r + 1):
            coefficient = (-1) ** k * binomial(r, k)  # Compute the binomial coefficient with alternating signs
            term = coefficient * x ** (r - k)  # Compute the term
            expanded_form += term  # Add the term to the expanded form

        return expanded_form

    @staticmethod
    def polyremainder1(n, a):
        # # Define the symbol
        # x = symbols('x')
        #
        # # Initialize an empty expression for the expanded form
        # expanded_form = 0
        #
        # # Iterate over the terms in the expansion
        # for k in range(n + 1):
        #     coefficient = binomial(n, k)  # Compute the binomial coefficient
        #     term = coefficient * x ** (n - k) * a ** k  # Compute the term
        #     expanded_form += term  # Add the term to the expanded form

        x = symbols('x')

        # Initialize an empty expression for the expanded form
        expanded_form = x ** n + a

        return expanded_form

    @staticmethod
    def polynomial_mod(expression, modulus):
        # Define the symbol
        x = symbols('x')

        # Extract the terms of the polynomial
        terms = expression.as_expr().as_ordered_terms()

        # Initialize an empty list to store the reduced terms
        reduced_terms = []

        # Iterate over each term and perform modulo operation
        for term in terms:
            exponent = term.as_poly(x).degree()
            coefficient = term.as_coefficient(x ** exponent)
            reduced_coefficient = coefficient % modulus
            if reduced_coefficient != 0:
                reduced_terms.append(reduced_coefficient * x ** exponent)

        # Sum up the reduced terms to form the reduced polynomial
        reduced_polynomial = sum(reduced_terms)

        return reduced_polynomial


    @staticmethod
    def smallest_r2(n):
        # Compute the target value for comparison
        target = math.log2(n) ** 2

        # Start with r = 2
        r = 2

        # Set a maximum limit for r
        max_r = 1000000

        # Iterate until the condition is satisfied or we reach the maximum limit
        while r <= max_r:
            # Compute the order of n modulo r
            order = 1
            while pow(n, order, r) != 1:
                order += 1

            # Check if the order is greater than the target
            if order > target:
                return r

            # Increment r for the next iteration
            r += 1
            print(r)

        # If the loop terminates without finding a suitable r, return None
        return None

n = 29
result = PrimeTester.smallest_r2(n)
print("Smallest value of r for n =", n, ":", result)

# binomial expansion of Power[\(40)x+ a\(41),n] for n = 31 and r = 31
