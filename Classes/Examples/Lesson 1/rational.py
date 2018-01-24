import math
class Rational:
    # instance methods
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator,denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
    
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator) 
    
    def to_float(self):
        return self.numerator / self.denominator
    
    def multiply(self, other):
        return Rational(self.numerator*other.numerator,self.denominator*other.denominator)
    
def main():
    x = Rational(3,4)
    y = Rational(1,5)
    product = x.multiply(y)
    print( product )
    
if __name__ == "__main__":
    main()
