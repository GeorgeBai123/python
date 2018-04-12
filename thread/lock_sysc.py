#coding=UTF-8
import threading
import time

def sub():
    global num
    temp=num
    time.sleep(0.0001)
    # time.sleep(0.1)
    num=temp-1
    time.sleep(2)
num=100


l=[]
s=time.time()
for i in range(100):
    t=threading.Thread(target=sub,args=())
    t.start()
    l.append(t)
for i in l:
    i.join()

print(time.time() - s)
print(num)

# 首次定义一个全局变量num=100,然后开辟了100个子线程，但是Python的那把GIL锁
# 限制了同一时刻只能有一个线程使用cpu，所以这100个线程是处于抢这把锁的状态，
# 谁抢到了，谁就可以运行自己的代码。在最开始的情况下，每个线程抢到cpu，
# 马上执行了对全局变量减一的操作，所以不会出现问题。但是我们改动后，
# 在全局变量减一之前，让他睡了0.1秒，程序睡着了，cpu可不能一直等着这个线程，
# 当这个线程处于I/O阻塞的时候，其他线程就又可以抢cpu了，所以其他线程抢到了，
# 开始执行代码，要知道0.1秒对于cpu的运行来说已经很长时间了，这段时间足够让
# 第一个线程还没睡醒的时候，其他线程都抢到过cpu一次了。他们拿到的num都是100，
# 等他们醒来后，执行的操作都是100-1,所以最后结果是99.同样的道理，如果睡的时
# 间短一点，变成0.001，可能情况就是当第91个线程第一次抢到cpu的时候，第一个线
# 程已经睡醒了，并修改了全局变量。所以这第91个线程拿到的全局变量就是99，然后第
# 二个第三个线程陆续醒过来，分别修改了全局变量，所以最后结果就是一个不可知的数了。
