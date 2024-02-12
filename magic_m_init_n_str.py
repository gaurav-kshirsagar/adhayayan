# Magic methods in python

#Without magic method:
'''
class MyClass:
    def greet(self):
        print("GM")

myobj = MyClass()       #OBJECT CREATION --> BLANK O/P
print(myobj)            #OBJECT PRINTING --> O/P > Memory location

myobj.greet()           #Calling function through object o/p "GM"
'''

#With Magic method:

class Myclass:
    def __init__(self):
        print('__init__ called')
    
    def __str__(self):
        print('__str__ called')
        return "Hello"

myobj = Myclass()       #OBJECT CREATION --> __init__ called
print(myobj)            #OBJECT PRINTING --> __str__ called

class Myclass:
    def __init__(self):
        print('__init__ called')
    
    def __str__(self):
        print('__str__ called')
        return "Hello"

myobj = Myclass()       #OBJECT CREATION --> __init__ called
print(myobj)            #OBJECT PRINTING --> __str__ called

class Student:
    def __init__(self,r,n,m,c):
        self.rn = r
        self.name = n
        self.marks = m
        self.city = c

    def __str__(self):
        return f"RN = {self.rn} name = {self.name} marks = {self.name} city={self.city}"

s1 = Student(1,'abcd',10,'pune')
print(s1)

s2 = Student(2,'abcdefg',20,'mumbai')
print(s2)
