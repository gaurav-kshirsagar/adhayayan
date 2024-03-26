# threading

'''
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
'''
#method base threading

from threading import Thread

class Evennum(Thread):
    def run(self):
        for i in range(0,21,2):
            print(i)

t1 = Evennum()
t1.start() # START automatically invokes run method
'''
#class base thread
from threading import Thread

class EvennumGen(Thread):
    def __init__(self,end):
        self.end = end
        super(). __init__()

    def run(self):
        for i in range(0,self,end):
            print(i)

t1 = EvennumGen(31)
t1.start()















