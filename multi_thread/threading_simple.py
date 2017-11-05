import threading
import time


def worker():
    print('Starting', threading.current_thread().getName())
    time.sleep(0.2)
    print('Exiting', threading.current_thread().getName())


def my_service():
    print('Starting', threading.current_thread().getName())
    time.sleep(0.3)
    print('Exiting', threading.current_thread().getName())


t = threading.Thread(name='My_Service', target=my_service)
w = threading.Thread(name='Worker-1', target=worker)
w2 = threading.Thread(name='Worker-2',target=worker)  # use default name

w.start()
w2.start()
t.start()
