from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        if denom != 0:
            self.numer = numer
            self.denom = denom
            self._clean()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        result = Rational((self.numer * other.denom + other.numer * self.denom), (self.denom * other.denom))
        result._clean()
        return result

    def __sub__(self, other):
        result = Rational((self.numer * other.denom - other.numer * self.denom), (self.denom * other.denom))
        result._clean()
        return result

    def __mul__(self, other):
        result = Rational((self.numer * other.numer), (self.denom * other.denom))
        result._clean()
        return result

    def __truediv__(self, other):
        if (other.numer * self.denom != 0):
            result = Rational((self.numer * other.denom), (self.denom * other.numer))
            result._clean()
            return result

    def __abs__(self):
        result = Rational((abs(self.numer)), (abs(self.denom)))
        result._clean()
        return result

    def __pow__(self, power):
        if power > 0:
            result = Rational((self.numer ** power), (self.denom ** power))
            result._clean()
        elif power < 0:
            result = Rational((self.denom ** abs(power)), (self.numer ** abs(power)))
            result._clean()
        elif power == 0:
            result = Rational(1, 1)
            result._clean()
        return result

    def __rpow__(self, base):
        if (((self.numer > 0) and (self.denom > 0)) or ((self.numer < 0) and (self.denom < 0))):
            result = float(base ** (self.numer / self.denom))
        elif (((self.numer < 0) and (self.denom > 0)) or ((self.numer > 0) and (self.denom < 0))):
            result = float(1 / (base ** (abs(self.numer) / abs(self.denom))))
        elif self.numer == 0:
            result = float(1)
        return result

    def _fixzero(self):
        """account for 0 fractions"""
        if self.numer == 0:
            self.denom = 1

    def _reduce(self):
        """calculate the Greatest Common Denominator"""
        x = self.numer
        y = self.denom
        while(y):
            x, y = y, x % y 
        """reduce the fraction"""
        if (self.numer != 0) and (self.denom != 0):
            self.numer = int(self.numer / x)
            self.denom = int(self.denom / x)

    def _clean(self):
        self._fixzero()
        self._reduce()