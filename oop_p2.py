'''
class Myclass:
    x = 10
    def m1(self):
        print("M1 of my class called")

class Otherclass(Myclass):
    x = 90
    y = 20
    def m2(self):
        print("m2 of otherclass called")

myobj = Myclass()
otherobj = Otherclass()

print(myobj.x)
#print(myobj.y)

myobj.m1()
#myobj.m2()

print(otherobj.x)
print(otherobj.y)
otherobj.m1()
otherobj.m2()

class Calculator:
    def add(self,a,b):
        print("add= ", a+b)
    def sub(self,a,b):
        print("sub= ",a-b)
    def mul(self,a,b):
        print("mul= ",a*b)
    def div(self,a,b):
        print("div= ",a/b)

class Advcalc(Calculator):
    def square(self,a):
        print("square= ",a*a)
    def cube(self,a):
        print("cube= ",a*a*a)

advcal = Advcalc()

advcal.add(10,11)
advcal.sub(20,10)
advcal.mul(10,5)
advcal.div(10,5)
advcal.square(2)
advcal.cube(5)

#multiple inheritance:

class A:
    x = 5
    z = 99
class B:
    x = 10
    y = 20
class C(B,A):
    pass

cobj = C()
print(cobj.x)
print(cobj.y)
print(cobj.z)
'''
'''
#multilevel inh

class A:
    x = 10
class B(A):
    x = 100
class C(B):
    x = 1000
class D(C):
    x = 10000

dobj = D()
print(dobj.x)


#Hierarchical Inh:

class A:
    x = 10
class B(A):
    y = 20
class C(A):
    z = 30

bobj = B()
cobj = C()

print(bobj.x)
print(bobj.y)
#print(bobj.z) sibling can not access the property.
print()

print(cobj.x)
print(cobj.z)
print(cobj.y)

#function overloadig
#from multipledispatch import dispatch

@dispatch(int,int)
def add(a,b):
    print("add= ",a+b)
    
@dispatch(int,int,int)
def add(a,b,c):
    print("add= ",a+b+c)

add(10,20)
add(10,20,30)

#method overloading
from multipledispatch import dispatch

class Myclass:
    @dispatch(int,int)
    def add(a,b):
        print('add= ',a+b)

    @dispatch(int,int,int)
    def add(a,b,c):
        print('add= ',a+b+c)

    @dispatch(str,str)
    def add(a,b):
        print('add= ',a+b)

myobj = Myclass()
myobj.add(10,20)
myobj.add(10,20,30)
myobj.add('Pune','Mumbai')

#method overriding:

class Calc:
    def div(self,a,b):
        ans = a/b
        print("div= ",ans)

class Advcalc:
    def sqr(self,n):
        ans = n*n
        print("Square= ",ans)

    def div(self,a,b):
        ans = a/b
        q = a//b
        r = a%b
        print("Div= ",ans)
        print("Q= ",q)
        print("R= ",r)

advobj = Advcalc()

advobj.sqr(3)
advobj.div(10,5)
'''

#Duck Typeing:

class Honda:
    def max_speed(self):
        print("Max speed of honda is 220 KMPH")

    def fuel_type(self):
        print("Fuel type is Disel")

    def transmission(self):
        print("Transmission of HOnda is manual")

class Skoda:
    def max_speed(self):
        print('Max speed of skoda is 240 KMPH')

    def fuel_type(self):
        print('Fuel type of skoda is Petrol')

city = Honda()
slavia = Skoda()

def get_car_info(obj):
    obj.max_speed()
    obj.fuel_type()

get_car_info(slavia)

    

























































