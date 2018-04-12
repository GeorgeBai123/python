#coding=UTF-8
import  threading
import time


def demo(m):
	print(m)
	time.sleep(2)
	print('step 2')
t1 = threading.Thread(target=demo,args=('Hellow\n',))
# t1.setDaemon(True)
t1.start()


#isAlive(): 返回线程是否处于活动中
print(t1.isAlive())
#getName(): 返回线程名
print(t1.getName())
#threading.currentThread():返回当前的线程变量
print(threading.currentThread())
#threading.enumerate():返回一个包含正在运行的线程的列表
print(threading.enumerate())
#threading.activeCount():返回正在运行的线程数量
print(threading.activeCount())

t1.join()
print('end')
