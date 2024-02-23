# Abstraction :


from abc import ABC, abstractmethod

'''
class Myclass(ABC):
    def m1(self):
        print('Hello from m1 of Myclass')

    @abstractmethod
    def m2(self):
        pass

#myobj = Myclass()
#myobj.m1

class Subclass(Myclass):
    def m2(self):
        print('Hello from m2 of sub class')

chobj = Subclass()
chobj.m1()
chobj.m2()
'''

class RBI(ABC):
    def new_guidelines(self):
        print('REPO rate is incresed by 0.7% ')
        print('3rd parties can NOT store credit card details')
        print('KYC is mandatory evry 2yrs')

    @abstractmethod
    def intrest_rate(self):
            pass

#r = RBI()
#r.new_guidelines()

class IDFC(RBI):
    def intrest_rate(self):
        print('intrest rate in IDFC is 4.5%')

i = IDFC()
i.new_guidelines()
i.intrest_rate()

print()
class HDFC(RBI):
    def intrest_rate(self):
        print('intrest rate in HDFC is 3.5%')

h = HDFC()
h.new_guidelines()
h.intrest_rate()
