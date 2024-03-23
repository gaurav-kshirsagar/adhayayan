#encapsulation
'''
class Myclass:
    x = 90
    _y = 100
    __Z = 110

myobj =  Myclass()

print(myobj.x)
print(myobj._y)
print(myobj.__z)


class Car:
    model = ''
    __maxspeed = 200

    def setMaxspeed(self,ms):
        self.__maxspeed = ms

    def getMaxspeed(self):
        return self.__maxspeed

c1 = Car()
c1.model = 'Nexon'
print(c1.model)
#print(c1.__maxspeed)   it will throw error
c1.setMaxspeed(320)
print(c1.getMaxspeed())
'''

#abstraction
from abc import ABC,abstractmethod

class Myclass(ABC):
    def m1(self):
        print('M1 from myclass')

    @abstractmethod
    def m2(self):
        pass

#myobj = Myclass()

class Subclass(Myclass):
    def m2(self):
        print('M2 from subclass')

subobj = Subclass()
subobj.m1()
subobj.m2()
