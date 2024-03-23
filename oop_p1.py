# OOP

'''
class Student:
    rn = 0
    name = ''
    city = ''

    def getData(self):
        print(self.rn)
        print(self.name)
        print(self.city)


s1 = Student()
s1.rn = 1
s1.name = 'abs'
s1.city = 'pune'

s2 = Student()
s2.rn = 2
s2.name = 'gsk'
s2.city = 'nagar'

s1.getData()
s2.getData()
'''

'''
class Myclass:
    def __init__(self):
        print('__init__called')

    def __str__(self):
        print('__str__called')
        return "Hello"
    
myobj = Myclass ()
print(myobj)
'''

class Student:
    def __init__(self,r,n,m,c):
        self. rn = r
        self. name = n
        self. marks = m
        self. city = c

    def __str__(self):
        return f"RN = {self.rn} Name = {self.name} Marks = {self.marks} city = {self.city} "

s1 = Student(1,'abc',10,'Pune')
print(s1)
