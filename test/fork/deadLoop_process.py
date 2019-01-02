import os
from multiprocessing import Pool

def loop(name):
    x = 0
    while True:
        x = x ^ 1

if __name__=='__main__':
    print('parent process %s' % os.getpid())

    p = Pool(3)  # 同时运行的进程数，和cpu 核心数相同最好
    for i in range(3):
        p.apply_async(loop, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')