import time
from threading import Thread
class even(Thread):
    def run(self):
        for i in range(100):
            if i%2==0:
                print(i)
                # time.sleep(2)
class  odd(Thread):
    def run(self):
        for i in range(100):
            if i%2!=0:
                print(i)
                # time.sleep(2)
t1=even()
t2=odd()
t1.start()
# t1.join()
t2.start()
# t2.join()
# t1.start()
# time.sleep(0.5)
# t2.start()