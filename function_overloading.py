'''
- whenever we are having two or more than two funcions with the same name 
BUT different signature this is called as function overloading.
- Differnent signature - either different no. of args must be there or 
different types of args must be there.
- python does not supports the concept of overloading, BUT still we can achieve it through
a 3rd party library named as 'multipledispatch'
-pip install multiple dispatch
'''

from multipledispatch import dispatch

@dispatch(int,int)
def add(a,b):
    print('add fun with 2 int called')
    ans = a + b
    print(ans)

@dispatch(str,str)
def add(a,b):
    print('add fun with 2 str called')
    ans = a + b
    print(ans)

@dispatch(int,int,int)
def add(a,b,c):
    print('add fun with 3 int called')
    ans = a + b + c
    print(ans)

add(10,20,30)
add(10,20)
add('Pune','Python')