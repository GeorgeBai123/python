#coding=UTF-8
import threading,time

class myThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		self.foo()
		# print('\n')
		self.bar()
	def foo(self):
		LockA.acquire()
		print('I am foo-%s GET LockA------%s' %(self.name,time.ctime()))

		LockB.acquire()
		print('I am foo-%s GET LockB------%s' %(self.name,time.ctime()))
		

		LockB.release()
		time.sleep(1)
		LockA.release()
	def bar(self):
		LockB.acquire()
		print('I am bar-%s GET LockB------%s' %(self.name,time.ctime()))

		LockA.acquire()
		print('I am bar-%s GET LockA------%s' %(self.name,time.ctime()))

		LockA.release()
		LockB.release()

LockA=threading.Lock()
LockB=threading.Lock()

t=myThread()
t.start()

t=myThread()
t.start()

# for i in range(10):
# 	t=myThread()
# 	t.start()


# 线程2在等待线程1释放B锁，线程1在等待线程2释放A锁，互相制约