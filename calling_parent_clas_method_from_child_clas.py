# Calling a parent class method from child class method

class Person:
    def __init__(self,n,a,g):
        print('Person class called')
        self.name = n
        self.age = a
        self.gender = g
        
    def __str__(self):
        return f"Name = {self.name},Age = {self.age},Gender = {self.gender}"

class Student(Person):
    def __init__(self,n,a,g,r,m):
        print('Student class init called')
        super().__init__(n,a,g)
        self.rn = r
        self.marks = m

    def __str__(self):
        person_data = super().__str__()
        return f"{person_data},RN = {self.rn}, Marks = {self.marks}"

class Teacher(Person):
    def __init__(self,n,a,g,i,s):
        print('teacher class init called')
        super().__init__(n,a,g)
        self.eid = i
        self.sal = s

    def __str__(self):
        person_data = super().__str__()
        return f"{person_data},EID = {self.eid}, Salary ={self.sal}"

s1 = Student('Stu1',10,'M',1,98)
t1 = Teacher('Tech1',40,'F',121,12000)
print(s1)
print(t1)
    
