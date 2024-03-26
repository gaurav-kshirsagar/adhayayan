from threading import Thread

class MyThread(Thread):
    def __init__(self,start,stop):
        self.st = start
        self.sp = stop
        super().__init__()

    def print_range(self):
        for i in range(self.st,self.sp):
            print(i)

    def run(self):
        self.print_range()

t1 = MyThread(0,21)
t2 = MyThread(40,61)
print('Thread start')
t1.start()
t2.start()
print('Thraed End')
