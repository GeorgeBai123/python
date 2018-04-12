#coding=UTF-8
import Queue,threading

#队列里只有put和get两个方法，列表的那些方法都没有
#join是用来阻塞进程，与task_done配合使用才有意义。可以用Event对象来理解，每次put()，join里面的计数器加1,每次task_done（），计数器减1，计数器为0的时候，才能进行下次put（）


q=Queue.Queue()

def foo():
	q.put(111)
	q.put(222)
	q.put(333)
	q.join() #有个join，程序就停在这里
	print('ok') 
def bar():
	print(q.get())
	q.task_done()
	print(q.get())
	q.task_done()
	print(q.get())
	q.task_done() #要在每个get()语句后面都加上

t1=threading.Thread(target=foo,args=())
t1.start()
t2=threading.Thread(target=bar,args=())
t2.start()

#t1,t2谁先谁后无所谓，因为会阻塞住，等待信号
