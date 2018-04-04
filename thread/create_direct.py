# coding=UTF-8
import threading
import time


def foo(n,p):
    print('>>>>>>>>>>>>>>>%s-%s\n' % (n,p))
    time.sleep(3)
    print('tread 1')


t1 = threading.Thread(target=foo, args=(2,3))
# arg后面一定是元组，t1就是创建的子线程对象
t1.start()  # 把子进程运行起来
#主线程中创建了一个子线程

print('ending')



