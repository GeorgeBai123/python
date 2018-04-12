#coding=UTF-8
import threading
import time

def add():
    global num
    lock.acquire()
    temp=num
    # time.sleep(0.001)
    time.sleep(0.1)
    num=temp+1
    lock.release()
    time.sleep(2)
    
num=0
l=[]
lock=threading.Lock()

for i in range(100):
    t=threading.Thread(target=add,args=())
    t.start()
    l.append(t)

for i in l:
    i.join()
print(num)