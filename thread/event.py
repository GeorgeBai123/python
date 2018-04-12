#coding=UTF-8
import threading,time

# event.isSet()：返回event的状态值；

# event.wait()：如果 event.isSet()==False将阻塞线程；

# event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；设置对象的时候，默认是False的

# event.clear()：恢复event的状态值为False。

event=threading.Event()  #创建一个event对象

def foo():
	print('wait.........')
	event.wait()
 	#event.wait(1)#if event 对象内的标志位为Flase,则阻塞
 	#wait()里面的参数的意思是：只等待1秒，如果1秒后还没有把标志位改过来，就不等了，继续执行下面的代码
 	print('connect to redis server')

print('attempt to start redis server')

time.sleep(3)
event.set()

for i in range(5):
	t=threading.Thread(target=foo,args=())
	t.start()
#3秒之后，主线程结束，但子线程并不是守护线程，子线程还没结束，所以，程序并没有结束，应该是在3秒之后，把标志位设为true，即event.set（）

