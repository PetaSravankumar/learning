import time
from threading import Thread
class Task1(Thread):
    def run(self):
        l=["rattu",'mithil',"shanu"]
        for i in l:
            print(i)
            time.sleep(3)
# class  Task2(Thread):
#     def run(self):
#         for i in range(10):
#             print(i)
#             time.sleep(2)
# class Task3:
#     def run(self):
#         a=10
#         b=20
#         c=a+b
