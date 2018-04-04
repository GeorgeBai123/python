#coding=UTF-8
import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print('ok')
        time.sleep(2)
        print('end')


t1 = MyThread()  # 创建线程对象
t1.start()  # 激活线程对象
print('end again')  # 建议使用直接创建的方式