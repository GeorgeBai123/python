#coding=UTF-8
import threading,time

class MyThread(threading.Thread):
    def __init(self):
        threading.Thread.__init__(self)

    def run(self):

        self.foo()
        self.bar()
    def foo(self):
        LockA.acquire()
        print('i am %s GET LOCKA------%s'%(self.name,time.ctime()))
        #每个线程有个默认的名字，self.name就获取这个名字

        LockB.acquire()
        print('i am %s GET LOCKB-----%s'%(self.name,time.ctime()))

        LockB.release()
        time.sleep(1)
        LockA.release()

    def bar(self):#与
        LockB.acquire()
        print('i am %s GET LOCKB------%s'%(self.name,time.ctime()))
        #每个线程有个默认的名字，self.name就获取这个名字

        LockA.acquire()
        print('i am %s GET LOCKA-----%s'%(self.name,time.ctime()))

        LockA.release()
        LockB.release()

LockA=threading.Lock()
LockB=threading.Lock()

# for i in range(10):
    t=MyThread()
    t.start()

#线程2在等待线程1释放B锁，线程1在等待线程2释放A锁，互相制约
#我们在用互斥锁的时候，一旦用的锁多了，很容易就出现这种问题

#运行结果:
#i am Thread-1 GET LOCKA------Sun Jul 23 11:25:48 2017
#i am Thread-1 GET LOCKB-----Sun Jul 23 11:25:48 2017
#i am Thread-1 GET LOCKB------Sun Jul 23 11:25:49 2017
#i am Thread-2 GET LOCKA------Sun Jul 23 11:25:49 2017
#然后就卡住了
#
#死锁示例