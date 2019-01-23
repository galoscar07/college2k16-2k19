'''
Created on Nov 1, 2016

@author: Arthur
'''

class RationalNumber:
    # Class field, will be shared by all the instances
    numberOfInstances =0
    """
      Abstract data type rational numbers
      Domain: {a/b  where a,b integer numbers, b!=0, greatest common divisor a, b =1}
    """
    def __init__(self, a, b):
        """
          Initialise a rational number
          a,b inteer numbers
        """
        self.__nominator = a
        self.__denominor = b


    def getDenominator(self):
        """
           Getter method
           return the denominator of the rational number
        """
        return self.__denominor

    def getNominator(self):
        """"
          Getter method
          return the nominator of the method
        """
        return self.__nominator

    @staticmethod
    def getTotalNumberOfInstances():
        """
          Get the number of created rational number instances
          return integer
        """
        return RationalNumber.numberOfInstances


    def add(self, a):
        """
        add 2 rational numbers
        a is a rational number
        Return the sum of two rational numbers as an instance of rational number.
        Raise ValueError if the denominators are zero.
        """
        if self.getDenominator() == 0 or a.getDenominator() == 0:
            raise ValueError("0 denominator not allowed")
        c = [self.getNominator()* a.getDenominator() + self.getDenominator() * a.getNominator(), self.getDenominator() * a.getDenominator()]
        d = self.__gcd(c[0], c[1])
        c[0] = c[0] // d
        c[1] = c[1] // d
        return RationalNumber(c[0], c[1])

    def __gcd(self, a, b):
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

    def __add__(self, other):
        """
          Overload + operator
          other  - rational number
          return a rational number, the sum of self and other
        """
        return self.add(other)

    def getFloat(self):
        """
          Get the real value for the rational number
          return a float
        """
        return float(self.getNominator())/self.getDenominator()

    def __lt__(self, ot):
        """
          Compare 2 rational numbers (less than)
          self the current instance
          ot a rational number
          return True if self<ot, False otherwise
        """
        if self.getFloat()<ot.getFloat(): return True
        return False

    def __str__(self):
        """
          provide a string representation for the rational number
          return a string
        """
        return str(self.__nominator)+"/"+str(self.__denominor)

    def __eq__(self, other):
        """
          Verify if 2 rational numbers are equals
          other - a rational number
          return True if the instance is equal with other
        """
        return self.__nominator==other.__nominator and self.__denominor==other.__denominor

def test_rational_add():
    r1 = RationalNumber(1, 2)
    r2 = RationalNumber(1, 3)
    r3 = r1.add(r2)
    assert r3.getNominator()==5
    assert r3.getDenominator()==6
    assert r3==RationalNumber(5, 6)

    #assert rational_add([1, 2], [1, 2]) == [1, 1]

def testEqual():
    """
      test function for testing == for 2 rational numbers
    """
    r1 = RationalNumber(1, 3)
    assert r1==r1
    r2 = RationalNumber(1, 3)
    assert r1==r2
    r1 = RationalNumber(1, 3)
    r1 = r1.add(RationalNumber(2, 3))
    r2 = RationalNumber(1, 1)
    assert r1==r2


def testCompareOperator():
    """
    Test function for < >
    """
    r1 = RationalNumber(1, 3)
    r2 = RationalNumber(2, 3)
    assert r2>r1
    assert r1<r2

def testAddOperator():
    """
      Test function for the + operator
    """
    r1 = RationalNumber(1, 3)
    r2 = RationalNumber(1, 3)
    r3 = r1+r2
    assert r3 == RationalNumber(2, 3)

def testCreate():
    """
      Test function for creating rational numbers
    """
    r1 = RationalNumber(1,3)  #create the rational number 1/3
    assert r1.getNominator()==1
    assert r1.getDenominator()==3
    r1 = RationalNumber(4,3)  #create the rational number 4/3
    assert r1.getNominator()==4
    assert r1.getDenominator()==3

testCreate()
testEqual()
test_rational_add()
testAddOperator()
testCompareOperator()
