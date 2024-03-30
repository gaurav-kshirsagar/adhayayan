# class base decorator

'''
class Deco:
    def __init__(self,func):
        self.func = func #self.func = function


    def __call__(self):
        print('*'*10)
        self.func()     #function
        print('/'*10)

@Deco
def function():
    print('Hello')

#function = Deco(function)
function()
'''
#####
class Deco:
    def __init__(self,func):
        self.func = func

    def __call__(self,li):
        res = self.func(li)
        return res - res * 0.2

grocery = [10,20,70]

@Deco
def calc_bill(li):
    res = 0
    for i in li:
        res += i
    return res

print(calc_bill(grocery))


    
    
