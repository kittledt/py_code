import threading
import asyncio


#此代码演示2个任务并发
@asyncio.coroutine
def hello(n):
    print('Hello world! (%s-%d)' % (threading.currentThread(),n))
    yield from asyncio.sleep(n)
    print('Hello again! (%s-%d)' % (threading.currentThread(),n))

#创建事件循环loop
loop = asyncio.get_event_loop()
#task 对coroutine 对象再封装，或者task list
tasks = [hello(2), hello(5)]
#run_until_complete将协程注册到事件循环，并启动事件循环
loop.run_until_complete(asyncio.wait(tasks))
loop.close()