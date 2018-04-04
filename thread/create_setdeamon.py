#coding=UTF-8
import  threading
import time

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print('ok')
        time.sleep(2)
        print('end')

t1=MyThread()#创建线程对象
#线程完成后不用管子线程是否运行完都退出，就要设置setDaemon（True）
t1.setDaemon(True)
t1.start()#激活线程对象
print('end again')
#运行结果是马上打印ok和 end again 
#然后程序终止，不会打印end