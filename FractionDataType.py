class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __mul__(self,other):
        tempden=self.den*other.den
        tempnum=self.num*other.num
        return f"{tempnum}/{tempden}"
    def __add__(self,other):
          tempden=(self.num*other.den)+(self.den*other.num)
          tempnum=self.num*other.num
          return f"{tempnum}/{tempden}"
    def __sub__(self,other):
          tempden=(self.num*other.den)-(self.den*other.num)
          tempnum=self.num*other.num
          return f"{tempnum}/{tempden}"
    def __truediv__(self,other):
          tempden=other.den*self.den
          tempnum=self.den*other.num
          return f"{tempnum}/{tempden}"

a=Fraction(5,6)
b=Fraction(6,3)
print(a*b)
print(a+b)
print(a-b)
print(a/b)
