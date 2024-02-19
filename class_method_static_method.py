#class method and instance method , static method:
'''
class Student:
    school = 'PMC School'       #class var

    @classmethod
    def setschool(cls,s):       #class method
        cls.school = s

    def __init__(self,r,s1,s2):     #instance var
        self.rn = r
        self.sem1 = s1
        self.sem2 = s2

    def setRn(self,r):          #Instance method
        self.rn = r

    @staticmethod
    def avg_marks(s1,s2):       #static method
        avg_marks = (s1+s2)/2
        print('avg_marks=',avg_marks)

s1 = Student(1,80,90)
s2 = Student(2,60,70)

s2.setRn(3)                         #instance method(args...)
Student.setschool('NewSchool')      #class method(args..)

print("s1.rn=",s1.rn)
print("s1.sem1=",s1.sem1)
print("s1.sem2=",s1.sem2)
print("s1.school=",s1.school)

print()

print("s2.rn=",s2.rn)
print("s2.sem1=",s2.sem1)
print("s2.sem2=",s2.sem2)
print("s2.school=",s2.school)

Student.avg_marks(40,50)

'''
class Student:
    school = 'PMC School'       #class var

    @classmethod
    def setschool(cls,s):       #class method
        cls.school = s

    def __init__(self,r):     #instance var
        self.rn = r

    def setRn(self,r):          #Instance method
        self.rn = r

    @staticmethod
    def check_rn(r):            #static method
        if r<= 0:
            return False
        else:
            return True


roll_no = int(input("Enter Roll No:"))
if Student.check_rn(roll_no):
    s3 = Student(roll_no)
else:
    print("Invalid Roll no, can not create Object")


s1 = Student(1)
s2 = Student(2)

s2.setRn(98)
print(s1.school)
print(s2.school)

print()

Student.setschool('NewSchool')
print(s1.school)
print(s2.school)
