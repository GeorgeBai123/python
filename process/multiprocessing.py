#coding=UTF-8

import multiprocessing
import time

def foo():
	print('ok')
	time.sleep(2)

if __name__ == '__main__':
	p=multiprocessing.Process(target=foo,args=())
	p.start()
	print('ending')