#coding=UTF-8

from multiprocessing import Pipe,Process


def foo(sk):
	sk.send('hello') #主进程发消息
	print(sk,recv()) #主进程收消息

sock,conn=Pipe() #创建了管道的两头
if __name__ == '__main__':
	
	p=Process(target=foo,args=(sock,))
	p.start()

	print(conn.recv())  #子进程收消息
	conn.send('hi son') #子进程发消息