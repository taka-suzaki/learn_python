import threading
import time

def func1():
    time.sleep(1)
    print("func1")
    
def func2():
    print("func2")

thread = threading.Thread(target=func1)
thread.start()
func2()
