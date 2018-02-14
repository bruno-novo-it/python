# Aula 16 - Thread's
 # Executar tarefas concorrencialmente

from threading import Thread
import time

def my_func(i):
    print("Iniciando a Thread %d" % i)
    time.sleep(5)
    print("Thread %d finalizada" % i)

for i in range(10):
    t  = Thread(target=my_func, args=(i,))
    t.start()