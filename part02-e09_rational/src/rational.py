#!/usr/bin/env python3

class Rational(object):
    def __init__(self,a:int,b:int):
        self.numerator = a
        self.denominator = b
    
    def __str__(self):
        return f"{self.numerator} / {self.denominator}"
    
    def __add__(self,rational):
        result_numerator =  self.numerator*rational.denominator + rational.numerator*self.denominator
        result_denominator = self.denominator*rational.denominator
        return Rational(result_numerator,result_denominator)

    
    def __mul__(self,rational):
        result_numerator = self.numerator*rational.numerator
        result_denominator = self.denominator*rational.denominator
        return Rational(result_numerator,result_denominator)
    
    def __truediv__(self,rational):
        result_numerator = self.numerator*rational.denominator
        result_denominator = self.denominator*rational.numerator
        return Rational(result_numerator,result_denominator)


    def __sub__(self,rational):
        result_numerator =  self.numerator*rational.denominator - rational.numerator*self.denominator
        result_denominator = self.denominator*rational.denominator
        return Rational(result_numerator,result_denominator)
        
    def __eq__(self, value):
        return self.numerator == value.numerator and self.denominator == value.denominator
    
    def __gt__(self,rational):
        return self.numerator*rational.denominator > self.denominator*rational.numerator
    
    def __lt__(self, rational):
        return self.numerator*rational.denominator < self.denominator*rational.numerator


def main():
    r1=Rational(1,2)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
