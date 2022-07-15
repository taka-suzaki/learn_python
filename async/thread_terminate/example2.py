# Python program using
# traces to kill threads

import sys
import trace
import threading
import time


class ThreadWithTrace(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run	
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def terminate(self):
        self.killed = True

def func(name="Taro"):
    while True:
        print(f'{name}: thread running')
        time.sleep(1)

        
t1 = ThreadWithTrace(target = func)
t2 = ThreadWithTrace(target=func, args=("Jiro",))
t1.start()
t2.start()
time.sleep(4)
t1.terminate()
time.sleep(2)
t2.terminate()
t1.join()
# time.sleep(.1)
if not t1.is_alive():
    print('thread killed')
