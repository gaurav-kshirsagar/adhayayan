#calling a parent class method from chhild class method

class Parentclass:
    def greet(self):
        print("Good morning from Parentclass greet")

class Childclass(Parentclass):
    def greet(self):
        print("Good morning from Childclass greet")
        #Parentclass.greet(self)
        super().greet() #super().method(args)

childobj = Childclass()
childobj.greet()

'''
class Person:
    def __init__(self,n,a,g):
        print('Person class called')
        self.name = n
        self.age = a
        self.gender = g

    def __str__(self):
        return f"Name=(self.name),Age=(self.age),Gender=(self.gender)"
    
class Student(Person):
    def __init__(self,n,a,g,r,m):
        print('Student class init called')
        super().__init__(n,a,g)
        self.rn = r
        self.marks = m

    def __str__(self):
        person_data = super().__str__()
        return f"{person_data},RN=(self.rn),MARKS=(self.marks)"
    
class Teacher(Person):
    def __init__(self,n,a,g,i,s):
        print('Teacher class init called')
        super().__init__(n,a,g)
        self.eid = i
        self.sal = s

    def __str__(self):
        person_data = super().__str__()
        return f"{person_data},EID=(self.eid),SAL=(self.sal)"

s1 = Student('stu1',10,'M',1,98.34)
t1 = Teacher('tch1',45,'F',101,10000)

print(s1)
print(t1)
'''
