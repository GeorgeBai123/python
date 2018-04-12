#coding=UTF-8
import Queue

#队列里读写数据只有put和get两个方法，列表的那些方法都没有
q=Queue.Queue()  #创建一个队列对象  FIFO先进先出
#q=queue.Queue(20)
#这里面可以有一个参数，设置最大存的数据量，可以理解为最大有几个格子
#如果设置参数为20，第21次put的时候，程序就会阻塞住，直到有空位置，也就是有数据被get走

# Queue.get_nowait() 相当Queue.get(False)


# 非阻塞 Queue.put(item) 写入队列，timeout等待时间
# Queue.put_nowait(item) 相当Queue.put(item, False)
q.put(11)
q.put('hello')
q.put(3.14)


#返回队列的大小
print(q.qsize())
#如果队列为空，返回True,反之False
print(q.empty()) 
#如果队列满了，返回True,反之False
print(q.full()) 

# Queue.get([block[, timeout]])获取队列，timeout等待时间
print(q.get()) 
print(q.get())
print(q.get())
#默认阻塞，等待put一个数据
#print(q.get()) 



# Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
# Queue.join() 实际上意味着等到队列为空，再执行别的操作