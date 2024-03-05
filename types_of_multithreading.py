# Multithreading 
# Method Based thread:
'''
from threading import Thread

class NumGen:
    def even(self):
        for i in range(0,21,2):
            print(i)
            
    def odd(self):
        for i in range(1,21,2):
            print(i)

ng =NumGen()

t1=Thread(target=ng.even)
t2=Thread(target=ng.odd)
t1.start()
t2.start()
'''

# Class Based Thread:
'''
from threading import Thread

class EvenNumGenerator(Thread):
    def run(self):
        for i in range(0,21,2):
            print(i)

class OddNumGenerator(Thread):
    def run(self):
        for i in range(1,21,2):
            print(i)

t1 = EvenNumGenerator()
t2 = OddNumGenerator()

t1.start()
t2.start()
'''
# methods with argument
'''
from threading import Thread

def even(end):
    for i in range(0,end,2):
        print(i)

def odd(end):
    for i in range(1,end,2):
        print(i)

t1 = Thread(target=even,args= (21,))
t2 = Thread(target=odd,args= (21,))
t1.start()
t2.start()

'''
from threading import Thread

class EvenNumGenerator(Thread):
    def __init__(self,end):
        self.end = end
        super().__init__()
        
    def run(self):
        for i in range(0,21,2):
            print(i)

class OddNumGenerator(Thread):
    def run(self):
        for i in range(1,21,2):
            print(i)

t1 = EvenNumGenerator(31)
t2 = OddNumGenerator()

t1.start()
t2.start()





    
