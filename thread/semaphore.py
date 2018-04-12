#coding=UTF-8
import threading
import time

semaphore=threading.Semaphore(5)

def foo():
	global num
	semaphore.acquire()
	temp=num
	time.sleep(2)
	num=temp-1
	print('ok')
	semaphore.release()
l=[]
num=10
for i in range(10):
    t=threading.Thread(target=foo,args=())
    t.start()
    l.append(t)

for i in l:
	i.join()
print(num)


# 也是一把锁，可以指定有几个线程可以同时获得这把锁，比如设置最多是5个