# task 1
'''
class Company:
    def trainee(self):
        print('Hello this is a trainee')

    def team_lead(self):
        print('Hello this is a Team lead')

    def manager(self):
        print('Hello manager this side')

    def seniormanager(self):
        print('Hello this is a senior manager')

    def director(self):
        print('Hello this is a director')

    def seniordirector(self):
        print('Hello this is a senior manger')

    def vicepresident(self):
        print("Hello this is a vice precident")

cobj = Company()

cobj.trainee()
cobj.team_lead()
cobj.manager()
cobj.seniormanager()
cobj.director()


class Mobile:
    def apple(self):
        print('this is apple iphone mobile')

    def samsung(self):
        print('this is samsung mobile')

    def redmi(self):
        print('this is redmi mobile')

mobj = Mobile()

mobj.redmi()
'''

class Animal:
    name = ''
    age = 0

class Dog(Animal):
    pass

class Cat(Animal):
    pass

cobj = Cat()

print(cobj.name)
print(cobj.age)