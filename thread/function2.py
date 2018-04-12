#coding=UTF-8
import  threading
import time

class myThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(m):
		print(m)
		time.sleep(2)
		print('step 2')
t2 = myThread()
# t2.setDaemon(True)
t2.start()
# t2.join()

#isAlive(): 返回线程是否处于活动中
print(t2.isAlive())
#getName(): 返回线程名
print(t2.getName())
#threading.currentThread():返回当前的线程变量
print(threading.currentThread())
#threading.enumerate():返回一个包含正在运行的线程的列表
print(threading.enumerate())
#threading.activeCount():返回正在运行的线程数量
print(threading.activeCount())



print('real end ')