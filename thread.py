import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def thread1():
    logging.debug('start1')
    time.sleep(3)
    logging.debug('end1')

def thread2(x, y=0):
    logging.debug('start2')
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    logging.debug('end2')

if __name__ == '__main__':
    t1 = threading.Thread(name='rename thread', target=thread1)
    t2 = threading.Thread( kwargs={'x': 100, 'y': 5}, target=thread2)
    t1.start()
    t2.start()
    print('started')