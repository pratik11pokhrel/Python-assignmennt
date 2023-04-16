#Q1

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except Exception:
    print("Cannot square non-numeric characters")

#Q2

try:
    x = int(input("Enter an integer: "))
    sqr = x ** 2
    print(f"You entered {x}, your number squared is {sqr}.")
except:
    print("Unrecognized number! Please try again!")
#Q3

class Line:
    dis = 0
    
    def __init__(self, coordinateA, coordinateB):
        self.a = coordinateA[0]
        self.b = coordinateB[0]
        self.c = coordinateA[1]
        self.d = coordinateB[1]
    
    def distance(self):
        return ((self.b - self.a)**2 + (self.d - self.c)**2)**0.5
    
    def slope(self):
        self.distance
        try:
            return ((self.d-self.c)/(self.b-self.a))
        except Exception:
            return print("Infinity")
    
c1 = (3,2)
c2 = (8,10)
myLine = Line(c1, c2)

print(myLine.distance())
print(myLine.slope())


#Q4

class Cylinder:
    def __init__(self,height=1,radius=1):
        self.hei = height
        self.rad = radius
        
    def volume(self):
        return 3.14 * self.rad ** 2 * self.hei
    
    def surface_area(self):
        return 2 * 3.14 * self.rad * (self.rad + self.hei)
    
h = 20
r = 10
cyl = Cylinder(h ,r)
print(cyl.volume())
print(cyl.surface_area())

#Q5

class InputOutString:
    
    def getString(self):
        y = input("Enter a string: ")
        self.y = y
    
    def printString(self):
        self.getString()
        upr = self.y.upper()
        print(upr)

x = InputOutString()
x.printString()
#Q6

with open('myfile.txt',"r") as f, open('myfile1.txt',"w") as f1:
    for line in f:
        f1.write(line)
#Q7

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
x = lambda a, b : a ** 2 + b ** 2
print(x(num1,num2))