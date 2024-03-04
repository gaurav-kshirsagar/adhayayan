# Multithreading in Python
'''
# Single Thread / Main Thread:

def evens():
    for i in range(0,21,2):
        print(i)
        
def odds():
    for i in range(1,21,2):
        print(i)

evens()
odds()

#Multi threading:

from threading import Thread

def evens():
    for i in range(0,21,2):
        print(i)
        
def odds():
    for i in range(1,21,2):
        print(i)

t1 = Thread(target=evens)
t2 = Thread(target=odds)

t1.start()
t2.start()
'''

from threading import Thread, current_thread
print('Program Starts', current_thread().name)
def evens():
    for i in range(0,21,2):
        print(i,current_thread().name)
        
def odds():
    for i in range(1,21,2):
        print(i,current_thread().name)

t1 = Thread(target=evens)
t2 = Thread(target=odds)

t1.start()
t2.start()
print('Program Ends', current_thread().name)


