import math

class Rational:
    #class methods
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator,denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
        
    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)

    def to_float(self):
        return self.numerator / self.denominator

    def multiply(self, other):
        return Rational(self.numerator*other.numerator, self.denominator*other.denominator)

def main():
    x = Rational(3,7)
    y = Rational(2,5)
    product = x.multiply(y)
    print( product )
    
   
    
if __name__ == "__main__":
    main()