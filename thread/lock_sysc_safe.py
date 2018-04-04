#coding=UTF-8
import threading
import time

def sub():

    global num
    lock.acquire()#获取锁
    temp=num
    time.sleep(0.001)

    num=temp-1
    lock.release()#释放锁
    time.sleep(2)
num=100


l=[]
lock=threading.Lock()
for i in range(100):
    t=threading.Thread(target=sub,args=())
    t.start()
    l.append(t)
for i in l:
    i.join()

print(num)