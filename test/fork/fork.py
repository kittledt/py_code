import os

print('process %s start. ' % os.getpid())

pid = os.fork()        # Only works on Unix/Linux/Mac:
if pid == 0 :
    print ('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))