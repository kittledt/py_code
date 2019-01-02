# -*-coding=utf-8-*-

from multiprocessing import Process, Queue
from multiprocessing import Pool
import os,time,random
import  subprocess

def run_process(name):
    print('run child process %s (%s)'% (name, os.getpid()))

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__=='__main__':
    print('parent process %s' % os.getpid())
    p = Process(target = run_process, args= ('test',))   #创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
    print('child process will start')
    p.start()
    p.join()    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('child process end')

    p = Pool(4)               # 同时运行的进程数，和cpu 核心数相同最好
    for i in range(5):        # 0-4，创建并运行共5个进程
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

    #启动一个子进程，打开cmd，输入命令
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

    # 启动一个子进程，打开cmd，先打开，后交互输入
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\nbaidu.com\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)


    # 进程通信,在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()