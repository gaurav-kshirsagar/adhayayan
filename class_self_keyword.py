# Importance of self keyword
# whenever we call a method through an object, the object itself get passsed 
# as one of argument
# To hold the object which is being passed internally, We've to use "Self" keyword..
# Self keyword always holds the current object through which method got called.
class NewClass:
    '''This is NewClass'''
    def greet(self):
        print("self=",self)
        print("Good Morning")

    def add(self,a,b):
        ans = a + b
        print(ans)

new_obj = NewClass()
print("new_obj=",new_obj)
new_obj.greet()
new_obj.add(10,20)
# Docstring = print(NewClass.__doc__)

print()
class Student:
    rn = 0
    name = ''
    city = ''

    def getData(self):
        print(self.rn)
        print(self.name)
        print(self.city)

s1 = Student()

s1.rn = 10
s1.name = 'abc'
s1.city = 'Pune'

s1.getData()

s2 = Student()

s2.rn = 11
s2.name = 'xyv'
s2.city = 'mumbai'

s2.getData()
