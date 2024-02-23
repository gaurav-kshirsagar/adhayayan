# Encapsulation:
'''
class Myclass:
    x = 10          #public
    _y = 20         #protected = public
    __z = 30        #private

myobj = Myclass()
print(myobj.x)          #10
print(myobj._y)         #20
print(myobj.__z)        #ERROR
'''

class Car:
    model = ''              #Public
    __max_speed = 200       #Private

    def setMaxSpeed(self,ms):
        self.__max_speed = ms

    def getMaxSpeed(self):
        return self.__max_speed

c1 = Car()
c1.model = 'Altroz'

print(c1.model)
#print(c1.__max_speed)       #AttributeError
print(c1.getMaxSpeed())
c1.setMaxSpeed(240)
print(c1.getMaxSpeed())