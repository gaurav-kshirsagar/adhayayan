# Method overloading and method overriding

# Method overloading
'''
from multipledispatch import dispatch

class Myclass:
    @dispatch(int,int)
    def add(self,a,b):
        ans = a + b
        print('addition of 2 int is :', ans)
        
    @dispatch(str,str)
    def add(self,a,b):
        ans = a + b
        print('concatination of 2 str is :', ans)

    @dispatch(int,int,int)
    def add(self,a,b,c):
        ans = a + b
        print('addition of 3 int is :', ans)

myobj = Myclass()

myobj.add(10,20)
myobj.add(10,20,30)
myobj.add('Python-','Django')
'''

# Method overriding

class Calc:
    def div(self,a,b):
        ans = a / b
        print('div = ',ans)

class AdvCalc(Calc):
    def sqr(self,n):
        ans = n*n
        print('square= ',ans)

    def div(self,a,b):
        ans = a / b
        Q = a // b
        R = a % b
        print('Q= ',Q)
        print('R= ',R)
        print('div= ',ans)

advobj = AdvCalc()

advobj.sqr(3)
advobj.div(10,20)
