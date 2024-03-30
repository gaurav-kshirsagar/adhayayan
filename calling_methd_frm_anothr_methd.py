# calling a method from another method:
'''
class Myclass:
    def m1(self):
        print('m1 of Myclass called')

class Otherclass:
    def m2(self):
        print('m2 of other class called')
        Myclass.m1(self)

otherobj = Otherclass()
otherobj.m2()
'''

# calling a parent class method from child class
# super >>> super().method(args)

class Person:
    def __init__(self,n,a,g):
        print('Person class called')
        self.name = n
        self.age  = a
        self.gender = g

    def __str__(self):
        return f"Name = {self.name}, Age= {self.age}, Gender= {self.gender}"


class Student(Person):
    def __init__(self,n,a,g,r,m):
        print('Student class init called')
        super().__init__(n,a,g)
        self.rn = r
        self.marks = m

    def __str__(self):
        person_data = super().__str__()
        return f"{person_data},RN = {self.rn}, Marks= {self.marks}"

class Teacher(Person):
    def __init__(self,n,a,g,i,s):
        print('Teacher class init called')
        super().__init__(n,a,g)
        self.eid = i
        self.sal = s

    def __str__(self):
        person_data = super().__str__()
        return f"{person_data}, EID= {self.eid}, Sal= {self.sal}"

s1 = Student('Abc',14,'M',31,98)
t1 = Teacher('xvy',43,'F',121,25000)

print(s1)
print(t1)
