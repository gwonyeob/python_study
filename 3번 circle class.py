import math

class Circle:
    radi = 0
    peri = 0

    def __init__(x, y):
        x.radi = y
        x.peri = round(math.pi,2)*x.radi*2

    def calcPerimeter(x):
        circumference=round(x.peri,2)
        print("원의 둘레:", circumference)

    def calcArea(x):
        area=x.peri*x.radi/2
        print("원의 면적:", area)

number= int(input("반지름을 입력하세요  >>  "))
special = Circle(number)
special.calcPerimeter()
special.calcArea()