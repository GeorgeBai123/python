#coding=UTF-8
import threading
import time


def foo(n):
    print('>>>>>>>>>>>>>>>%s' % n)
    time.sleep(n)

    print('tread 1')


def bar(n):
    print('>>>>>>>>>>>>>>>>%s' % n)
    time.sleep(n)
    print('thread 2')


s = time.time()
t1 = threading.Thread(target=foo, args=(1,))
t1.start()  # 把子进程运行起来

t2 = threading.Thread(target=bar, args=(2,))
t2.start()

t1.join()  # 只是会阻挡主线程运行，跟t2没关系
t2.join()
print(time.time() - s)
print('ending')


#这个方法的作用是：在子线程完成运行之前，这个子线程的父线程将一直等待子线程运行完再运行

''' 运行结果： 
>>>>>>>>>>>>>>>2
>>>>>>>>>>>>>>>>5 
tread 1 
thread 2 
5.001286268234253 
ending 

'''