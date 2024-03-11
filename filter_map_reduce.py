# Lambda, Filter,map,reduce

#fun = lambda arg1,arg2: arg1+arg2
#print(fun(10,20))


#Filter:
'''
li = [10,20,30,40,50]
def function(param1):
    return param1>20

res = filter(function,li)
res = map(lambda x: x>20,li)
print(list(res))
'''

string = 'aerioutyk'
def function(param1):
    print(param1)
    if param1 in 'aeiou':
        return True
    else:
        return False
res = filter(function,string)
print(list(res))

#map:
'''
li1 = [10,20,30,40,50]
li2 = [1,2,3,4,5]
def function(param1,param2):
    return param1+param2

#res = map(function,li1,li2)
res = map(lambda x,y: x+y,li1,li2)
print(list(res))
'''

#reduce:
'''
from functools import reduce

li = [1,2,3,4,5]

def function(a,b):
    return  a+b

#res = reduce(function,li)
#res = reduce(lambda x,y: x+y,li)
print(res)
'''

