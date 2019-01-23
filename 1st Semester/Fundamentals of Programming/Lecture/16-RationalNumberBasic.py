class Rational:
    def __init__(self,nom,denom):
        if denom == 0:
            raise ValueError("Denominator must be non-0")

        g = self._gcd(nom,denom)

        self._nom = nom // g        
        self._denom = denom // g

    def getNominator(self):
        return self._nom

    def getDenominator(self):
        return self._denom

    def setNominator(self,n):
        self._nom = n

    def setDenominator(self,d):
        if d == 0:
            raise ValueError("Denominator must be non-0")
        self._denom = d

    def _gcd(self, a, b):
        """
        Return the greatest common divisor of two positive integers.
        Raise ValueError if the parameters are negative integers.
        """
        if a < 0 or b < 0:
            raise ValueError("a and b must be greater than 0")
        if a == 0 and b == 0:
            raise ValueError("gcd(0, 0) is undefined")
        if a == 0:
            return b
        else:
            if b == 0:
                return a
            else:
                while a != b:
                    if a > b:
                        a = a - b
                    else:
                        b = b - a
                return a

    def __str__(self):
        if self.getDenominator() == 1:
            return str(self.getNominator())
        return str(self.getNominator())+"/"+str(self.getDenominator())

    def add(self, q2):
        if type(q2) == int:
            q2 = Rational(q2,1)
        
        nom = self.getNominator() * q2.getDenominator() + q2.getNominator() * self.getDenominator()
        denom = self.getDenominator() * q2.getDenominator()

        return Rational(nom,denom)

    def __add__(self, q):
        return self.add(q)

def testRational():
    q = Rational(1,2)
    assert q.getNominator() == 1 and q.getDenominator() == 2

    q = Rational(1000,2000)
    assert q.getNominator() == 1 and q.getDenominator() == 2
    
    try:
        q = Rational(2,0)
        assert False
    except ValueError as ve:
        pass
    try:
        q = Rational(2,1)
        q.setDenominator(0)
        assert False
    except ValueError as ve:
        pass

    assert str(Rational(1,2))=="1/2"
    assert str(Rational(2,1))=="2"

testRational()

globals()
locals()
