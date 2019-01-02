import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)



# 假定这是你的银行存款:
balance = 0
balance_lock = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

#without lock
def run_thread(n):
    for i in range(100000):
        change_it(n)

#with lock
def change_it_lock(n):
    # 先存后取，结果应该为0:
    global balance_lock
    balance_lock = balance_lock + n
    balance_lock = balance_lock - n

def lock_run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()            #当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
        try:
            # 放心地改吧:
            change_it_lock(n)
        finally:
            # 改完了一定要释放锁:       获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
            lock.release()

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# modify balance
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#with lock
t1 = threading.Thread(target=lock_run_thread, args=(5,))
t2 = threading.Thread(target=lock_run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance_lock)


# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()