import logging
import threading
import time


def worker():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def my_service():
    logging.debug('Starting')
    time.sleep(0.3)
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s (%(threadName)-1s)',
)

t = threading.Thread(target=my_service)
w = threading.Thread(target=worker)
w2 = threading.Thread(target=worker)  # use default name

w.start()
w2.start()
t.start()
