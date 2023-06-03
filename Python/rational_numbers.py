import math

# Implement a class for rational numbers.
class Rational:
    """
    A rational number is defined as the quotient of two integers a and b, 
    called the numerator and denominator, respectively, where b != 0.
    """
    def __init__(self, numer, denom, /):
        if (numer != int(numer)) or (denom != int(denom)):
            raise TypeError("expecting integer factors")
        if denom == 0:
            raise ZeroDivisionError("division by zero")
        if numer == 0:
            self.numer = 0
            self.denom = 1
            return
        numer = int(numer)
        denom = int(denom)
        if denom < 0:
            numer = -numer
            denom = -denom
        gcd = math.gcd(numer, denom)
        self.numer = numer // gcd
        self.denom = denom // gcd

    def __eq__(self, other):
        return (self.numer == other.numer) and (self.denom == other.denom)

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer,
                        self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer,
                        self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer,
                        self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom,
                        self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        # Exponentiation of a given rational number to an integer power.
        if power >= 0:
            return Rational(pow(self.numer, power),
                            pow(self.denom, power))
        else:
            return Rational(pow(self.denom, -power),
                            pow(self.numer, -power))

    def __rpow__(self, base):
        # Exponentiation of a real number to a rational number.
        return pow(base, self.numer / self.denom)
