# Inheritance
'''
class Myclass:
    x = 10
    def m1(self):
        print('m1 of Myclass called..')
class Otherclass(Myclass):
    x = 90
    y = 20
    def m2(self):
        print('m2 of Otherclass called..')

myobj = Myclass()
otherobj = Otherclass()

#print(myobj.x)
#print(myobj.y)
#myobj.m1()
#myobj.m2()

print(otherobj.x)
print(otherobj.y)
otherobj.m1()
otherobj.m2()

'''

class Calculator:
    def add(self,a,b):
        print("Add=",a+b)
    def sub(self,a,b):
        print("sub=",a-b)
    def mul(self,a,b):
        print("Mul=",a*b)
    def div(self,a,b):
        print("Div=",a/b)

class AdvancedCalc(Calculator):
    def square(Self,n):
        print("Square=",n*n)
    def cube(self,n):
        print("Cube=",n*n*n)

advcalc = AdvancedCalc()

advcalc.square(5)
advcalc.cube(5)
advcalc.add(10,20)
advcalc.sub(10,20)
advcalc.mul(10,20)
advcalc.div(10,20)
