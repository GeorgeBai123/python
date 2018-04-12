#coding=UTF-8

import multiprocessing,threading

def foo(q):
	q.put([12,'hello',True])

if __name__ == '__main__':
	q=multiprocessing.Queue() #创建进程队列

	#创建一个子进程

	p=multiprocessing.Process(target=foo,args=(q,))
	#通过传参的方式把这个队列对象传给父进程
	p.start()

	print(q.get())