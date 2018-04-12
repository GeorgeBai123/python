#coding=UTF-8
import threading,time

class myThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		self.foo()
		print('\n')
		self.bar()
	def foo(self):
		RLock.acquire()
		print('I am foo-%s GET LOCKA------%s' %(self.name,time.ctime()))
		RLock.acquire()
		print('I am foo-%s GET LOCKB------%s' %(self.name,time.ctime()))

		RLock.release()
		time.sleep(1)
		RLock.release()
	def bar(self):
		RLock.acquire()
		print('I am bar-%s GET LOCKB------%s' %(self.name,time.ctime()))
		RLock.acquire()
		print('I am bar-%s GET LOCKA------%s' %(self.name,time.ctime()))
		RLock.release()
		RLock.release()

LockA=threading.Lock()
LockB=threading.Lock()
RLock=threading.RLock()

for i in range(10):
	t=myThread()
	t.start()